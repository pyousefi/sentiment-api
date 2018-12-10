from flask import Flask
from flask_restful import Api

from resources.predictsentiment import PredictSentiment
from resources.retraining import Retraining

import os

app = Flask(__name__)
api = Api(app)

api.add_resource(PredictSentiment, '/predict')
api.add_resource(Retraining, '/retrain')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=os.environ.get("PORT"))
    # app.run(debug=True, host="0.0.0.0", port=8080)
