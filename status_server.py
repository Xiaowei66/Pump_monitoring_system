from flask import Flask, jsonify, make_response
from flask_restplus import Resource, Api
from machine_learning.config import *

app = Flask(__name__)
api = Api(app)


@api.route("/status")
@api.response(200, 'Success')
class Status(Resource):

    def get(self):
        query = "SELECT id, error, address FROM Pumps ORDER BY error ASC "
        rows = query_db(query)

        return make_response(jsonify(rows), 200)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == '__main__':
    app.run(port=8500, debug=True)