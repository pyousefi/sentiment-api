from flask_restful import Resource, reqparse
from resources.nlpmodel import NLPModel

class Retraining(Resource):

    def polarity(value):
        for value_correct in range(5):
            if int(value) == value_correct:
                return value
        else:
            raise ValueError("Value is not between 0 and 4")

    parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
    parser.add_argument("sentence", type=str, required=True, help="Field required")
    parser.add_argument("polarity", type=polarity, required=True, help="Field required: polarity between 0 and 4")

    def __init__(self):
        self.model = NLPModel()

    def post(self):
        args = Retraining.parser.parse_args()
        sentence = args["sentence"]
        polarity = args["polarity"]

        return {"sentence": sentence, "polarity": polarity}
