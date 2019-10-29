import sqlite3

from flask import *
from flask_restplus import *
# import pytorch as torch
from pickle import *
import numpy as np
import sqlite3

app = Flask(__name__)
api = Api(app)

@api.route("/learning/")
@api.response(200, 'Success')
@api.response(404, 'Not Found')
class Learning(Resource):

    def post(self):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()

        sql = ''' SELECT * FROM Pumps; '''
        rows = cur.execute(sql)
        result = []
        model = load(open('model.pkl', 'rb'))

        for row in rows:
            id = row[0]
            address = row[2]

            sql = ''' SELECT * FROM States WHERE id = %d; ''' % id
            records = cur.execute(sql)[-3600 * 12:]
            matrix = []
            for record in records:
                matrix += [record[6], record[7], record[8], record[9], record[10], record[11]]

            a = np.array(matrix, dtype="float64")
            probability = "%.2f" % (model.predict_proba(a.reshape(1, -1))[0][1] * 100)
            result.append({"id": id, "address": address, "probability": probability})

        result.sort(key=lambda x: -1 * float(x["probability"][:-1]))

        return make_response(jsonify(result), 200)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9999, debug=True)