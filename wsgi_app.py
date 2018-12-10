from flask import Flask
from flask_restful import Api, Resource, reqparse
from resources.nlpmodel import NLPModel
from resources.parser import Parser
import numpy as np

app = Flask(__name__)
api = Api(app)

model = NLPModel()

parser = reqparse.RequestParser()
parser.add_argument('query')

class PredictSentiment(Resource):

    def get(self):
        # use parser and find the user's query
        args = parser.parse_args()
        user_query = args['query']

        # vectorize the user's query and make a prediction
        uq_vectorized = model.vectorizer_transform(np.array([user_query]))
        prediction = model.predict(uq_vectorized)
        pred_proba = model.predict_proba(uq_vectorized)

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

api.add_resource(PredictSentiment, '/')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=os.environ.get("PORT"))
    # app.run(debug=True, host="0.0.0.0", port=8080)
