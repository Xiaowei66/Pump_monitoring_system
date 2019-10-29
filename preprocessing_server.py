import datetime
import requests
import json
from machine_learning.config import *
from flask import Flask, jsonify, make_response, request
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

def print_json(json_data):
    print(json.dumps(json_data, indent=4, sort_keys=True))


def create_db():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    sql_create_pumps_table = """ CREATE TABLE IF NOT EXISTS Pumps (
                                            id INTEGER PRIMARY KEY,
                                            name TEXT,
                                            address TEXT,
                                            suburb TEXT,
                                            postcode TEXT,
                                            bearing INTEGER,
                                            temperature REAL,
                                            speed REAL,
                                            power REAL,
                                            axial_vibration REAL,
                                            radial_vibration REAL,
                                            tangential_vibration REAL,
                                            error INTEGER,
                                            probability REAL
                                            
                            ); """
    sql_create_states_table = """CREATE TABLE IF NOT EXISTS States (
                                                pump INTEGER REFERENCES Pump(id),
                                                time TEXT,
                                                bearing INTEGER,
                                                temperature REAL,
                                                speed REAL,
                                                power REAL,
                                                axial_vibration REAL,
                                                radial_vibration REAL,
                                                tangential_vibration REAL, 
                                                error INTEGER
                                ); """

    sql_create_user_table = """
        CREATE TABLE IF NOT EXISTS user (
            username TEXT  PRIMARY KEY,
            password TEXT,
            curr_token TEXT,
            user_type TEXT
        );
    """

    cursor.execute(sql_create_pumps_table)
    cursor.execute(sql_create_states_table)
    cursor.execute(sql_create_user_table)

    try:
        cursor.execute(
            """ INSERT INTO Pumps (id, name, address, suburb, postcode) VALUES (7037, "UNSW PUMP", "17 High Street", "Kensington", "2033");
                INSERT INTO Pumps (id, name, address, suburb, postcode) VALUES (1137, "UNSW PUMP", "17 Maxwell Rd", "Pagewood", " 2035");
                INSERT INTO Pumps (id, name, address, suburb, postcode) VALUES (3723, "UNSW PUMP", "1-49 Fraser Ave", "Eastgardens", "2036");
                INSERT INTO Pumps (id, name, address, suburb, postcode) VALUES (3743, "UNSW PUMP", "3-1 Rosebery Ave", "Zetland", "2017");
                INSERT INTO Pumps (id, name, address, suburb, postcode) VALUES (3744, "UNSW PUMP", "117-123 Perouse Rd", "Randwick", "2031");
                INSERT INTO Pumps (id, name, address, suburb, postcode) VALUES (5134, "UNSW PUMP", "18 High Street", "Kensington", "2033");
                INSERT INTO Pumps (id, name, address, suburb, postcode) VALUES (3677, "UNSW PUMP", "20 High Street", "Kensington", "2033");
                INSERT INTO Pumps (id, name, address, suburb, postcode) VALUES (3673, "UNSW PUMP", "19 Maxwell Rd", "Pagewood", "2035");
                INSERT INTO Pumps (id, name, address, suburb, postcode) VALUES (3644, "UNSW PUMP", "25 High Street", "Kensington", "2033");
                INSERT INTO Pumps (id, name, address, suburb, postcode) VALUES (3642, "UNSW PUMP", "21 Maxwell Rd", "Pagewood", "2035");
                
                INSERT INTO user VALUES ("admin", "admin", "admin","admin");
                
            """)
    except:
        pass

    conn.commit()


def fetch_data(url):
    response = requests.get(url)
    return response.json()


def get_pumps():
    conn = sqlite3.connect("data.db")
    result = [x for x in
              conn.cursor().execute("""select * from pumps;""").fetchall()]
    print(result)
    return result


create_db()


@api.route("/states")
@api.response(200, 'OK')
@api.response(201, 'CREATED')
@api.response(404, 'NOT FOUND')
class States(Resource):

    def post(self):
        # print(request.json)
        # print(get_pumps())


        json_data = request.json
        time = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')

        # print(request.json)

        conn = sqlite3.connect("data.db")
        cur = conn.cursor()

        error = 1

        if (float(json_data["temperature"]) >= 35 and float(json_data["temperature"]) <= 45) or \
                (float(json_data["speed"]) >= 2880 and float(json_data["speed"]) <= 2900) or (
                float(json_data["axial_vibration"]) >= 1.81 and float(json_data["axial_vibration"]) <= 4.8) or (
                float(json_data["radial_vibration"]) >= 1.81 and float(json_data["radial_vibration"]) <= 4.8) or (
                float(json_data["tangential_vibration"]) >= 1.81 and float(json_data["tangential_vibration"])<= 4.8):
            error = 0
        elif (float(json_data["temperature"]) > 45) or (float(json_data["speed"]) > 2900) or (
                float(json_data["axial_vibration"]) > 4.8 ) or (
                float(json_data["radial_vibration"]) > 4.8 ) or (
                float(json_data["tangential_vibration"]) > 4.8):
            error = -1


        sql = ''' INSERT INTO States(pump, bearing, temperature, speed, power, axial_vibration, radial_vibration, tangential_vibration, time, error)
                                              VALUES(?,?,?,?,?,?,?,?,?,?) '''
        cur.execute(sql, (
            json_data["id"], json_data["bearing"], json_data["temperature"], json_data["speed"], json_data["power"],
            json_data["axial_vibration"], json_data["radial_vibration"], json_data["tangential_vibration"],
            time, error))

        sql = ''' UPDATE Pumps SET bearing = ?, temperature = ?, speed = ?, power = ?, axial_vibration = ?, radial_vibration = ?, tangential_vibration = ?, error = ? WHERE id = ? '''
        cur.execute(sql, (
            json_data["bearing"], json_data["temperature"], json_data["speed"], json_data["power"],
            json_data["axial_vibration"], json_data["radial_vibration"], json_data["tangential_vibration"],
            error, json_data["id"]))

        conn.commit()

        return make_response(jsonify({'message': 'CREATED'}), 201)

    def get(self):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()

        sql = ''' SELECT * FROM Pumps order by id ;'''

        rows = cur.execute(sql).fetchall()
        result = []

        for row in rows:
            result.append({
                "id": row[0],
                "name": row[1],
                "address": row[2],
                "suburb": row[3],
                "postcode": row[4],
                "bearing": row[5],
                "temperature": row[6],
                "speed": row[7],
                "power": row[8],
                "axial_vibration": row[9],
                "radial_vibration": row[10],
                "tangential_vibration": row[11],
                "error": row[12]}
            )
        return make_response(jsonify(result), 200)



@api.route("/data")
@api.response(200, 'OK')
@api.response(201, 'CREATED')
@api.response(404, 'NOT FOUND')
class Percent(Resource):

    def get(self):
        pump_id = request.args.get("pump")
        temp = []
        nums = []

        query = """SELECT count(*) AS num FROM states WHERE pump = %s and error = 1"""\
                %(pump_id)
        rows = query_db(query)
        nums.append(rows[0]["num"])

        query = """SELECT count(*) AS num FROM states WHERE pump = %s and error = 0""" \
                % (pump_id)
        rows = query_db(query)
        nums.append(rows[0]["num"])

        query = """SELECT count(*) AS num FROM states WHERE pump = %s and error = -1""" \
                % (pump_id)
        rows = query_db(query)
        nums.append(rows[0]["num"])


        temp.append({
            "normal": nums[0],
            "warning": nums[1],
            "accident": nums[2]
        })

        return jsonify(temp)





@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == '__main__':
    app.run(port=7500, debug=True)
