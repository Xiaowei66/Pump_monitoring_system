import requests
import json
import csv
import time
from multiprocessing import Process


def post_data(file_name):
    while True:
        with open(file_name, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["BEARING_CONDITION"] == "" or row["BEARING_CONDITION"] == 0:
                    continue
                json_data = {"id": row["ASSET_ID"],
                             "bearing": row["BEARING_CONDITION"],
                             "temperature": row["SKIN_TEMPERATURE"],
                             "speed": row["SPEED"],
                             "power": row["OUTPUT_POWER"],
                             "axial_vibration": row["VIBRATION_AXIAL"],
                             "radial_vibration": row["VIBRATION_RADIAL"],
                             "tangential_vibration": row["VIBRATION_TANGENTIAL"]}
                requests.post("http://127.0.0.1:7500/states", json=json_data)
                time.sleep(1)

def print_json(json_data):
    print(json.dumps(json_data, indent=4, sort_keys=True))



def main():
    pump_7037 = Process(target=post_data, args = {"./pump_data/7037.csv"})
    pump_3744 = Process(target=post_data, args = {"./pump_data/3744.csv"})
    pump_3743 = Process(target=post_data, args = {"./pump_data/3743.csv"})
    pump_3723 = Process(target=post_data, args = {"./pump_data/3723.csv"})
    pump_1137 = Process(target=post_data, args = {"./pump_data/1137.csv"})
    pump_3642 = Process(target=post_data, args = {"./pump_data/3642.csv"})
    pump_3644 = Process(target=post_data, args = {"./pump_data/3644.csv"})
    pump_3673 = Process(target=post_data, args = {"./pump_data/3673.csv"})
    pump_3677 = Process(target=post_data, args = {"./pump_data/3677.csv"})
    pump_5134 = Process(target=post_data, args = {"./pump_data/5134.csv"})


    pump_7037.start()
    pump_3744.start()
    pump_3743.start()
    pump_3723.start()
    pump_1137.start()
    pump_3642.start()
    pump_3644.start()
    pump_3673.start()
    pump_3677.start()
    pump_5134.start()




if __name__ == '__main__':
    main()
