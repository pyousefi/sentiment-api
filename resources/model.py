from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
import os
from resources.nlpmodel import NLPModel

dir_path = os.path.dirname(os.path.abspath(__file__))
CLASSIFIER = dir_path + "/res/SentimentClassifier.pkl"
VECTORIZER = dir_path + "/res/TFIDFVectorizer.pkl"

class Model(Resource):

    def __init__(self):

        self.model = NLPModel()
        with open(CLASSIFIER, 'rb') as f:
            self.model.clf = pickle.load(f)

        with open(VECTORIZER, 'rb') as f:
            self.model.vectorizer = pickle.load(f)

    def get(self):

        return {"salut": "coco"}

    def post(self):
        pass
