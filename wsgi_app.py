from flask import Flask
from flask_restful import Api
from resources.model import Model
from resources.data import Data


app = Flask(__name__)
api = Api(app)

#api.add_resource(Model, '/Model', '/Model/<str:id>')
api.add_resource(Model, '/model')
api.add_resource(Data, '/data')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=os.environ.get("PORT"))
