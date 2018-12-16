from flask_restful import Resource, reqparse
from resources.nlpmodel import NLPModel
from pymongo import MongoClient
import os

MONGO = os.environ.get("MONGO", "localhost:27017")
dir_path = os.path.dirname(os.path.abspath(__file__))
STOPWORDS = dir_path + "/res/stopwords_nltk.txt"

class InsertSentence(Resource):

    def polarity(value):
        for value_correct in range(5):
            if int(value) == value_correct:
                return value
        else:
            raise ValueError("Value is not between 0 and 4")

    parser = reqparse.RequestParser()
    parser.add_argument("sentence", type=str, required=True, help="Field required")
    parser.add_argument("polarity", type=polarity, required=True, help="Field required: polarity between 0 and 4")

    def __init__(self):
        self.model = NLPModel()
        with open(STOPWORDS, "r") as f:
            stopwords = f.readlines()
        self.stopwords = [word.replace("\n", "") for word in stopwords]

    def post(self):
        args = InsertSentence.parser.parse_args()
        sentence = args["sentence"]
        polarity = args["polarity"]

        list_word = [word for word in sentence.split() if word not in self.stopwords]
        sentence = " ".join(list_word)

        client = MongoClient(MONGO)
        db = client["sentiment"]
        last_id = db["text"].find({"$query": {}, "$orderby": {"$natural": -1}})[0]["_id"]
        db["text"].insert_one({"_id": last_id+1, "sentence": sentence, "polarity": polarity})

        return {
            "sentence": sentence,
            "polarity": polarity,
            "id": last_id+1
        }

# TODO: delete and update sentence routes
