from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import database_operations

app = Flask(__name__)
api = Api(app)


class Potholes(Resource):
    def get(self):
        self.dbOps = database_operations.dbOps(
            "localhost", "root", "root", "techfiesta")
        potholeList = self.dbOps.fetchAll()
        potholeDictList = list()
        for sub in potholeList:
            tempDict = {
                "id": sub[0],
                "x_len": sub[1],
                "y_len": sub[2],
                "risk": sub[3],
                "confidence": sub[4]
            }
            potholeDictList.append(tempDict)
        return potholeDictList, 200

    def post(self):
        pass


api.add_resource(Potholes, '/potholes')

if __name__ == '__main__':
    app.run()
