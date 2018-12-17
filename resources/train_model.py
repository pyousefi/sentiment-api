import os
import pandas as pd
from pymongo import MongoClient
from resources.nlpmodel import NLPModel
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from flask_restful import Resource

MONGO = os.environ.get("MONGO", "localhost:27017")
client = MongoClient(MONGO)
db = client["sentiment"]

# At the moment, only polarities of 0 and 4 are considered (negative and positive)

class TrainModel(Resource):

    def post(self):

        model = NLPModel()
        cursor = db["text"].find()
        df = pd.DataFrame(list(cursor))
        pos_neg = df[(df['polarity'] == 0) | (df['polarity'] == 4)]

        pos_neg['Binary'] = pos_neg.apply(
            lambda x: 0 if x['polarity'] == 0 else 1, axis=1)

        model.vectorizer_fit(pos_neg.loc[:, 'sentence'])
        print('Vectorizer fit complete')

        X = model.vectorizer_transform(pos_neg.loc[:, 'sentence'])
        print('Vectorizer transform complete')
        y = pos_neg.loc[:, 'Binary']

        X_train, X_test, y_train, y_test = train_test_split(X, y)

        model.train(X_train, y_train)
        print('Model training complete')

        # TODO: archive pickles
        model.save_model()

        model.score = roc_auc_score(y_test, model.predict(X_test))

        return {
            "message": "Model has been retrained!",
            "score": model.score
        }
