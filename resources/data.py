import os
import sqlite3
from flask_restful import Resource

dir_path = os.path.dirname(os.path.abspath(__file__))
DATABASE = dir_path + "/res/compData.db"


class Data(Resource):

    def __init__(self):
        self.cursor = sqlite3.connect(DATABASE)

    def get(self):
        print("... DATABASE", DATABASE)
        query = "select * from training_patient"
        res = self.cursor.execute(query).fetchall()
        return {"res": res}

    def post(self):
        pass
