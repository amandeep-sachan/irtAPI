import numpy as np
import jsonpickle
import jsonpickle.ext.numpy as jsonpickle_numpy

from catsim.cat import generate_item_bank
# initialization package contains different initial proficiency estimation strategies
from catsim.initialization import *
# selection package contains different item selection strategies
from catsim.selection import *
# estimation package contains different proficiency estimation methods
from catsim.estimation import *
# stopping package contains different stopping criteria for the CAT
from catsim.stopping import *
from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

# to eliminate the error
jsonpickle_numpy.register_handlers()


class ItemResponseTheoryModel:
    #question bank is array of tuple [(question:Object, hardness:0.0 to 1.0)]
    #parameter_model is either '2PL', '3PL' or '4PL'
    def __init__(self, question_bank, parameter_model='2PL'):
        self.question_bank = question_bank
        self.question_bank_size = len(self.question_bank)
        assert self.question_bank_size > 0
        assert len(self.question_bank[0]) == 2
        self.indexed_items = generate_item_bank(self.question_bank_size, itemtype=parameter_model)
        self.parameter_model = parameter_model
        self.initializer = RandomInitializer()
        self.selector = MaxInfoSelector()
        self.estimator = HillClimbingEstimator()
        self.stopper = MaxItemStopper(self.question_bank_size)
        self.est_theta = self.initializer.initialize()
        self.responses = []
        self.administered_items = []
        for i in range(len(self.indexed_items)):
            self.indexed_items[i][1] = question_bank[i][1]
        
    #question_index is integer >= 0
    #answer is a boolean
    def answerQuestionAndEstimate(self, question_index, answer=False):
        assert question_index < self.question_bank_size
        self.responses.append(bool(answer))
        self.administered_items.append(int(question_index))
        new_est = self.estimator.estimate(items=self.indexed_items, administered_items=self.administered_items, response_vector=self.responses, est_theta=self.est_theta)
        self.est_theta = new_est
    
    #returns the next best question to ask -> returns tuple (index: integer, question: Object) 
    def getNextQuestionIndexToAsk(self):
        item_index = self.selector.select(items=self.indexed_items, administered_items=self.administered_items, est_theta=self.est_theta)
        return item_index, self.question_bank[item_index]

    # can be called after each question to know if we should stop asking further questions
    # this call is voluntary
    def shouldWeStopAskingQuestions(self):
        stop = self.stopper.stop(administered_items=self.indexed_items[self.administered_items], theta=self.est_theta)
        return stop




###################### FLASK APIs ###############################################


class InvalidUsage(Exception):
    def __init__(self, message):
        super(InvalidUsage, self).__init__()
        self.message = message


@app.route("/firstQuestion", methods=['POST'])
def question_first():
    """
    This function will create new object and initialize the parameters for ItemResponseTheoryModel.
    Then created object will call the function getNextQuestionIndexToAsk to get the question.
    Then it will send the question and object(in pickled format so that it can be reused).
    """
    if request.method == 'POST':
        #list of tuples containing questions along with difficulty level
        questionsList = []
        questions = request.data.get("questions")
        for ques in questions:
            tup = (ques["question"], ques["difficulty"])
            questionsList.append(tup)
        #print(questionsList)
        var = ItemResponseTheoryModel(questionsList)
        getQuestion = var.getNextQuestionIndexToAsk()
        pickled = jsonpickle.encode(var)
        resp = {"object": pickled, "index": getQuestion[0],"question": getQuestion[1][0], "difficulty": getQuestion[1][1]}

        return resp, status.HTTP_200_OK



@app.route("/nextQuestion", methods=['POST'])
def question_next():
    """
    List or create notes.
    """
    if request.method == 'POST':
        pickled = request.data.get("object")
        correct = request.data.get("correct")
        questionIndex = request.data.get("index")

        unPickled = jsonpickle.decode(pickled)

        unPickled.answerQuestionAndEstimate(questionIndex, correct)
        getQuestion = unPickled.getNextQuestionIndexToAsk()
        rePickled = jsonpickle.encode(unPickled)
        resp = {"object": rePickled, "index": getQuestion[0],"question": getQuestion[1][0], "difficulty": getQuestion[1][1]}
        
        return resp, status.HTTP_200_OK


@app.route("/stopQuestion", methods=['POST'])
def question_stop():
    """
    This endpoint tell us, whether to stop asking questions or not.
    """
    if request.method == 'POST':
        pickled = request.data.get("object")

        unPickled = jsonpickle.decode(pickled)

        boolean = unPickled.shouldWeStopAskingQuestions()
        message = ""
        if boolean:
            message = "You can stop asking questions."
        else:
            message = "You should not stop asking questions."
        resp = {"stop": boolean,"message": message}
        
        return resp, status.HTTP_200_OK



#Error handling
@app.errorhandler(404)
def page_not_found(e):
    return {"message": "Enter the correct url for endpoint."}, 404

@app.errorhandler(405)
def page_not_found(e):
    return {"message": "Type of http request is incorrect."}, 405

@app.errorhandler(500)
def page_not_found(e):
    return {"message": "Internal server error encountered. Pass the parameters in correct format."}, 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)