from flask_restful import Resource
from sklearn.ensemble import RandomForestClassifier

class Model(Resource):

    def __init__(self):
        self.model = RandomForestClassifier()

    def get(self):

        return {"salut": "coco"}

    def post(self):
        pass
