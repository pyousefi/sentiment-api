from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from resources.predictsentiment import PredictSentiment
from resources.data_manipulation import InsertSentence
from resources.train_model import TrainModel

import os

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

api.add_resource(PredictSentiment, '/predict')
api.add_resource(InsertSentence, '/insert')
api.add_resource(TrainModel, '/train')
#
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=os.environ.get("PORT"))
    # app.run(debug=True, host="0.0.0.0", port=8080)
