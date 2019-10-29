from flask import Flask, render_template, url_for, request, Response, redirect, session
from functools import wraps
import os
import sqlite3

# config for database

DATABASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data.db")

def connect_db():
    return sqlite3.connect(DATABASE)

def query_db(query, args=(), one=False):
    conn = connect_db()
    c = conn.cursor()
    cur = c.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    conn.commit()
    conn.close()
    return (rv[0] if rv else None) if one else rv



app = Flask(__name__)
app.config['SECRET_KEY'] = 'iot-project'


def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("token") is None:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("token") != "admin":
            return Response(status=404)
        return f(*args, **kwargs)
    return decorated_function





@app.route("/status", methods=["POST", "GET"])
@token_required
def index():
    return render_template("index.html", bar="index")


@app.route("/status/<id>", methods=["POST", "GET"])
@token_required
def index_id(id):
    return render_template("index.html", bar="index", id=id)


@app.route('/login/', methods=["POST", "GET"])
def login():
    return render_template("login.html")


@app.route('/history/', methods=["POST", "GET"])
@token_required
def history():
    return render_template("history.html", bar="history")


@app.route('/history/<id>', methods=["POST", "GET"])
@token_required
def history_id(id):
    return render_template("history.html", bar="history", id=id)


@app.route('/analysis', methods=["POST", "GET"])
@token_required
def analysis():
    return render_template("analysis.html", bar="analysis")


@app.route("/prediction", methods=["POST", "GET"])
@token_required
def prediction():
    return render_template("prediction.html", bar="prediction")


@app.route("/", methods=["POST", "GET"])
@token_required
def status():
    return render_template("status.html", bar="status")


@app.route("/admin-login/", methods=["POST", "GET"])
def dashboard():
    return render_template("admin_login.html")


@app.route("/admin-index/", methods=["POST", "GET"])
@admin_required
def admin_index():
    if request.method == "POST":
        username = request.form.get("phone")
        password = request.form.get("password")
        if username == "" or password == "":
            return render_template("admin_index.html", err="Invalid username or password")
        query = "insert into user(username, password) values ('%s', '%s')"%(username, password)
        query_db(query)
        return render_template("admin_index.html", mes="success to register")
    return render_template("admin_index.html")

@app.route("/update-user/", methods=["POST", "GET"])
@admin_required
def update_user():
    rows = query_db("select username from user;")
    return render_template("update_user.html", res=rows)


@app.route("/delete-user/<user>", methods=["POST", "GET"])
@admin_required
def delete_user(user):
    try:
        query_db("delete from user where username = '%s'"%(user))
    except:
        pass
    return redirect(url_for("update_user"))


@app.route("/admin_update/<user>", methods=["POST", "GET"])
@admin_required
def admin_update(user):
    if request.method == "POST":
        username = request.form.get("phone")
        password = request.form.get("password")

        if username == "" or password == "":
            return render_template("admin_update.html", err="Invalid username or password")
        query_db("update user set username='%s', password='%s' where username='%'"%(username, password, user))

    rows = query_db("select username, password from user;")
    return render_template("admin_update.html", res = rows[0])



@app.route("/take_token", methods=["POST", "GET"])
def take_token():
    session["token"] = request.args.get("token")
    return Response(status=200)


@app.route("/drop_token", methods=["POST", "GET"])
def drop_token():
    session.pop("token")
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True, port=5100, host='0.0.0.0')
