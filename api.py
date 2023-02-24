from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin
import pandas as pd
import ast
import database_operations

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)


class Potholes(Resource):
    @cross_origin()
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
        parser = reqparse.RequestParser()

        parser.add_argument('x_len', required=True)
        parser.add_argument('y_len', required=True)
        parser.add_argument('confidence', required=True)

        args = parser.parse_args()

        x_len = args['x_len']
        y_len = args['y_len']
        confidence = args['confidence']
        print(x_len)
        risk = self.__risk(x_len, y_len)

        values = {
            "x": x_len,
            "y": y_len,
            "confidence": confidence,
            "risk": risk
        }

        self.dbOps = database_operations.dbOps(
            "localhost", "root", "root", "techfiesta")
        self.dbOps.save(values=values)
        return "Added", 200

    def __risk(self, x_len, y_len):
        area = int(x_len) * int(y_len)

        if area < 45:
            return "LOW"
        elif area >= 45 and area <= 1125:
            return "MEDIUM"
        else:
            return "HIGH"


api.add_resource(Potholes, '/potholes')

if __name__ == '__main__':
    app.run()
