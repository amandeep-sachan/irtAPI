# Item Response Theory APIs

Item response theory (IRT), also known as latent trait theory or modern mental test theory; is a relatively new approach to psychometric test design. Whereas classical test theory focuses on the test as a whole, item response theory shifts its focus to the individual items (questions) themselves.

A number of parameters may be used when estimating the ability of a person using IRT:

    The 1 parameter logistic model (1PL) also known as the Rasch model, only uses item difficulty as a parameter for calculating a person’s ability.
    The 2 parameter logistic model (2PL) uses both item difficulty and item discrimination (the extent which the item is measuring the underlying psychological construct) as parameters.
    The 3 parameter logistic model (3PL) uses item difficulty, item discrimination and the extent which candidates can guess the correct answer, as parameters.

Regardless of the model used, IRT based tests have a number of advantages over classical test theory based tests. IRT allows item banking, which means that candidates can all be given a completely different set of items, but still provide an equally accurate estimate of ability. Also, IRT allows the use of adaptive testing, tests which tailor the difficulty of the test to each individual candidate. Increasingly, psychometricians are turning to IRT based models to design research and publish psychometric tests, with more research on IRT published every year. Similarly, most of the major test publishers, such as SHL and Saville consulting are using IRT based methods in their test development processes.

How will IRT affect test candidates?

Because IRT allows for item banking, test publishers can minimise the effects of cheating from unscrupulous candidates. With fixed form tests, candidates could print-screen their questions and share them among other candidates, giving them unfair advantages. With item banked tests, each candidate is given a unique set of questions, increasing test security. Also, IRT allows for adaptive testing, in which a test gets more, or less difficult depending on the performance of the candidate, tailoring the test to their ability. IRT provides myriad benefits to the test publisher, the client and the candidate, and IRT based models are becoming increasingly popular within psychometrics. 


# Requirement to use this API:
1. Python3
2. pip3
3. Install all the dependencies from requirements_python3.txt file using "pip3 install -R requirements_python3.txt"

# Steps to use this API:
1. Simply run the server using command "python3 serverFile.py"
2. There are 3 endpoints in this API:

	i) localhost:5000/firstQuestion        ----- POST

	ii) localhost:5000/nextQuestion        -----POST

	iii) localhost:5000/stopQuestion       -----POST
	


	i)Description of 1st endpoint:

	To hit this endpoint, pass array of objects containing questions in body(json format). For eg.:

	{"questions": [{"question": "aaaaa", "difficulty": 0.4}, {"question": "bbb", "difficulty": 0.8},{"question": "cc", "difficulty": 			0.2}, {"question": "dd", "difficulty": 0.6},{"question": "ee", "difficulty": 0.9}, {"question": "ff", "difficulty": 0.3}]}

	It will return the 'class object of model', 'content of question', 'difficulty' and 'index of question'.

	Sample Output:

		{
		"question": "cc",
		"object": "{\"responses\": [], \"administered_items\": [], \"stopper\": {\"_simulator\": null, \"py/object\": \"catsim.stopping.MaxItemStopper\", \"_max_itens\": 6}, \"indexed_items\": {\"base\": {\"dtype\": \"float64\", \"shape\": [4, 6], \"py/object\": \"numpy.ndarray\", \"byteorder\": \"<\", \"values\": \"eJxTfr1z+cfOL/Zm+neOnuj+bP9i7u2g0uBP9q/r73e6en21f+fo1NP7+Iv9gtPb3/0Q/2g/ayYI3ITSL6H0SXtjMHhsf/YMCLyB8i/bM5AFPtgTSwMAVdg8iQ==\"}, \"strides\": [8, 48], \"py/object\": \"numpy.ndarray\", \"dtype\": \"float64\", \"shape\": [6, 4]}, \"estimator\": {\"_verbose\": false, \"_precision\": 6, \"_evaluations\": 0, \"py/object\": \"catsim.estimation.HillClimbingEstimator\", \"_simulator\": null, \"_calls\": 0, \"_dodd\": false}, \"question_bank\": [{\"py/tuple\": [\"aaaaa\", 0.4]}, {\"py/tuple\": [\"bbb\", 0.8]}, {\"py/tuple\": [\"cc\", 0.2]}, {\"py/tuple\": [\"dd\", 0.6]}, {\"py/tuple\": [\"ee\", 0.9]}, {\"py/tuple\": [\"ff\", 0.3]}], \"selector\": {\"_simulator\": null, \"py/object\": \"catsim.selection.MaxInfoSelector\"}, \"est_theta\": -1.7131091026081933, \"initializer\": {\"_dist_type\": \"uniform\", \"_simulator\": null, \"_dist_params\": {\"py/tuple\": [-5, 5]}, \"py/object\": \"catsim.initialization.RandomInitializer\"}, \"question_bank_size\": 6, \"py/object\": \"__main__.ItemResponseTheoryModel\", \"parameter_model\": \"2PL\"}",
		"index": 2,
		"difficulty": 0.2
		}

	

	ii)Description of 2nd endpoint:

	You have to pass 3 parameters to this endpoint - 'answer of previous was correct or not', 'index of previous question' and 'class object of model that was returned previously'. 

	        Sample input:

		{
		"correct": false,
		"object": "{\"responses\": [], \"administered_items\": [], \"stopper\": {\"_simulator\": null, \"py/object\": \"catsim.stopping.MaxItemStopper\", \"_max_itens\": 6}, \"indexed_items\": {\"base\": {\"dtype\": \"float64\", \"shape\": [4, 6], \"py/object\": \"numpy.ndarray\", \"byteorder\": \"<\", \"values\": \"eJxTfr1z+cfOL/Zm+neOnuj+bP9i7u2g0uBP9q/r73e6en21f+fo1NP7+Iv9gtPb3/0Q/2g/ayYI3ITSL6H0SXtjMHhsf/YMCLyB8i/bM5AFPtgTSwMAVdg8iQ==\"}, \"strides\": [8, 48], \"py/object\": \"numpy.ndarray\", \"dtype\": \"float64\", \"shape\": [6, 4]}, \"estimator\": {\"_verbose\": false, \"_precision\": 6, \"_evaluations\": 0, \"py/object\": \"catsim.estimation.HillClimbingEstimator\", \"_simulator\": null, \"_calls\": 0, \"_dodd\": false}, \"question_bank\": [{\"py/tuple\": [\"aaaaa\", 0.4]}, {\"py/tuple\": [\"bbb\", 0.8]}, {\"py/tuple\": [\"cc\", 0.2]}, {\"py/tuple\": [\"dd\", 0.6]}, {\"py/tuple\": [\"ee\", 0.9]}, {\"py/tuple\": [\"ff\", 0.3]}], \"selector\": {\"_simulator\": null, \"py/object\": \"catsim.selection.MaxInfoSelector\"}, \"est_theta\": -1.7131091026081933, \"initializer\": {\"_dist_type\": \"uniform\", \"_simulator\": null, \"_dist_params\": {\"py/tuple\": [-5, 5]}, \"py/object\": \"catsim.initialization.RandomInitializer\"}, \"question_bank_size\": 6, \"py/object\": \"__main__.ItemResponseTheoryModel\", \"parameter_model\": \"2PL\"}",
		"index": 2
		}

	It will return the response as in last endpoint.


	iii)Description of 3rd endpoint:

	This endpoint simply tell us whether to stop or not at this point. You have to pass 'class object' and it will return the message.

	Sample input : 

		{
		"object": "{\"indexed_items\": {\"shape\": [6, 4], \"strides\": [8, 48], \"py/object\": \"numpy.ndarray\", \"base\": {\"shape\": [4, 6], \"values\": \"eJy7cTN1Vlb6G/tvFyS3yl96bl/0ydFPOvWz/dSHG3nZ1360XzLd4UV33mf7LzXHndd5fbWfNRMEbkLpl1D6pL0xGDy2P3sGBN5A+ZftGcgCH+yJpQGv4zn8\", \"py/object\": \"numpy.ndarray\", \"byteorder\": \"<\", \"dtype\": \"float64\"}, \"dtype\": \"float64\"}, \"py/object\": \"__main__.ItemResponseTheoryModel\", \"question_bank\": [{\"py/tuple\": [\"aaaaa\", 0.4]}, {\"py/tuple\": [\"bbb\", 0.8]}, {\"py/tuple\": [\"cc\", 0.2]}, {\"py/tuple\": [\"dd\", 0.6]}, {\"py/tuple\": [\"ee\", 0.9]}, {\"py/tuple\": [\"ff\", 0.3]}], \"selector\": {\"py/object\": \"catsim.selection.MaxInfoSelector\", \"_simulator\": null}, \"parameter_model\": \"2PL\", \"est_theta\": 4.813770229721193, \"responses\": [], \"administered_items\": [], \"initializer\": {\"_simulator\": null, \"_dist_params\": {\"py/tuple\": [-5, 5]}, \"py/object\": \"catsim.initialization.RandomInitializer\", \"_dist_type\": \"uniform\"}, \"stopper\": {\"_max_itens\": 6, \"py/object\": \"catsim.stopping.MaxItemStopper\", \"_simulator\": null}, \"estimator\": {\"_dodd\": false, \"py/object\": \"catsim.estimation.HillClimbingEstimator\", \"_calls\": 0, \"_simulator\": null, \"_precision\": 6, \"_verbose\": false, \"_evaluations\": 0}, \"question_bank_size\": 6}"
		}

	Sample output:

	{
		"stop": false,
		"message": "You should not stop asking questions."
	}
	
