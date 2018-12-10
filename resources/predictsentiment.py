from flask_restful import Api, Resource, reqparse
from resources.nlpmodel import NLPModel
import numpy as np

class PredictSentiment(Resource):

    parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
    parser.add_argument("query", type=str, required=True, help="Field required")

    def __init__(self):

        self.model = NLPModel()

    def get(self):
        # use parser and find the user's query
        args = PredictSentiment.parser.parse_args()
        user_query = args['query']

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
        confidence = round(pred_proba[0], 3)

        # create JSON object
        output = {'prediction': pred_text, 'confidence': confidence}

        return output
