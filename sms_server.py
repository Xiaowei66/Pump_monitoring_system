import nexmo
from flask import Flask, jsonify, make_response
from flask_restplus import Resource, Api, reqparse
from machine_learning.config import *

sms_client = nexmo.Client(key='7e1f7b82', secret='azy57VbJwb0XgPTs')
app = Flask(__name__)
api = Api(app)




@api.route("/message")
@api.response(200, 'Success')
class Message(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('send_from', type=str)
        parser.add_argument('send_to', type=str)
        parser.add_argument('content', type=str)

        args = parser.parse_args()

        send_from = args.get("send_from")
        send_to = args.get("send_to")
        content = args.get("content")

        if send_to == "all":
            admins = query_db("select username from user")
            for to in admins:
                message = sms_client.send_message({'from': send_from, 'to': to["username"], 'text': content})

        return make_response(jsonify({'message': "SUCCESS"}), 200)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == '__main__':
    app.run(port=7600, debug=True)