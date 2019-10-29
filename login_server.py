from flask import Flask, request
from flask_restplus import Resource, Api, abort
from machine_learning.config import *
import secrets

app = Flask(__name__)
api = Api(app)


@api.route("/login/")
@api.response(200, 'Success')
@api.response(400, 'Missing Username/Password')
@api.response(403, 'Invalid Username/Password')
class Login(Resource):

    def get(self):
        token = secrets.token_hex(32)
        username = request.args.get("username")
        password = request.args.get("password")

        print(username, password)

        sql = """SELECT * FROM user WHERE username = "%s" and password = "%s";""" % (username, password)
        u = query_db(sql)
        if len(u) == 0:
            abort(403, 'Invalid Username/Password')

        if username != "admin":
            sql = """UPDATE user set curr_token = '%s' where username = '%s'""" % (token, username)
            query_db(sql)
        else:
            res = query_db("select curr_token from user where username = '%s' "%(username))
            token = res[0]["curr_token"]

        return {'token': token}


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(port=7700, debug=True)
