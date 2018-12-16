from flask_restful import Api, Resource, reqparse
from resources.nlpmodel import NLPModel
import numpy as np
import unidecode
import os

dir_path = os.path.dirname(os.path.abspath(__file__))
STOPWORDS = dir_path + "/res/stopwords_nltk.txt"

class PredictSentiment(Resource):

    parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
    parser.add_argument("query", type=str, required=True, help="Field required")

    def __init__(self):

        self.model = NLPModel()
        with open(STOPWORDS, "r") as f:
            stopwords = f.readlines()
        self.stopwords = [word.replace("\n", "") for word in stopwords]

    def get(self):
        # use parser and find the user's query
        args = PredictSentiment.parser.parse_args()
        user_query = args['query']

        user_query = user_query.lower()
        user_query = unidecode.unidecode(user_query)

        list_word = [word for word in user_query.split() if word not in self.stopwords]
        user_query = " ".join(list_word)

        # vectorize the user's query and make a prediction
        uq_vectorized = self.model.vectorizer_transform(np.array([user_query]))
        prediction = self.model.predict(uq_vectorized)
        pred_proba = self.model.predict_proba(uq_vectorized)

        # Output either 'Negative' or 'Positive' along with the score
        if prediction == 0:
            pred_text = 'Negative'
        else:
            pred_text = 'Positive'

        # round the predict proba value and set to new variable
        if pred_text == "Positive":
            confidence = round(pred_proba[0], 3)
        else:
            confidence = 1-round(pred_proba[0], 3)

        # create JSON object
        output = {'prediction': pred_text, 'confidence': confidence}

        return output
