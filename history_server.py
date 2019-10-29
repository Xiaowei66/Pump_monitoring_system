from flask import Flask, jsonify, make_response,request
from flask_restplus import Resource, Api, reqparse
from machine_learning.config import *

app = Flask(__name__)
api = Api(app)

@api.route("/history/")
@api.response(200, 'Success')
class History(Resource):

    def get(self):
        pump_id = request.args.get("pump")

        query = """SELECT * FROM States WHERE pump = %s ORDER BY time DESC limit 30"""%(pump_id)
        rows = query_db(query)

        result = []

        for row in rows:
            result.append({
                "id": row["pump"],
                "time": row["time"],
                "temperature": row["temperature"],
                "speed": row["speed"],
                "power": row["power"],
                "bearing": row["bearing"],
                "axial_vibration": row["axial_vibration"],
                "radial_vibration": row["axial_vibration"],
                "tangential_vibration": row["axial_vibration"]}
            )

        return make_response(jsonify(result), 200)


    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('date', type=str)
        parser.add_argument('pump', type=str)
        args = parser.parse_args()
        date = "%"
        date += args.get("date") + "%"

        query = """SELECT * FROM States WHERE time like '%s' and pump = %s"""%(date, args.get('pump'))

        print(date)
        rows = query_db(query)
        result = []

        for row in rows:
            result.append({
                "id": row["pump"],
                "time": row["time"],
                "temperature": row["temperature"],
                "speed": row["speed"],
                "power": row["power"],
                "bearing": row["bearing"],
                "axial_vibration": row["axial_vibration"],
                "radial_vibration": row["axial_vibration"],
                "tangential_vibration": row["axial_vibration"]}
            )

        return make_response(jsonify(result), 200)



@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7800, debug=True)