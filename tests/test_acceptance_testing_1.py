import csv
import pytest
import requests
import time


def test_information_fields_correct():
    """
    Acceptance Testing 1.1
    Test that the information transmitted should include temperature, speed, output power and axial, radial, tangential of its vibration.
    """
    with open('../pump_data/1137.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        row = next(reader)

        assert ("BEARING_CONDITION" in row)
        assert ("ASSET_ID" in row)
        assert ("BEARING_CONDITION" in row)
        assert ("SKIN_TEMPERATURE" in row)
        assert ("SPEED" in row)
        assert ("OUTPUT_POWER" in row)
        assert ("VIBRATION_AXIAL" in row)
        assert ("VIBRATION_RADIAL" in row)
        assert ("VIBRATION_TANGENTIAL" in row)




def test_sensor_transmission_latency():
    """
    Acceptance Testing 1.2
    Test that the information should be received within 0.2 seconds of latency.
    """
    with open('../pump_data/1137.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        row = next(reader)

        start = time.time()
        json_data = {"id": row["ASSET_ID"],
                     "bearing": row["BEARING_CONDITION"],
                     "temperature": row["SKIN_TEMPERATURE"],
                     "speed": row["SPEED"],
                     "power": row["OUTPUT_POWER"],
                     "axial_vibration": row["VIBRATION_AXIAL"],
                     "radial_vibration": row["VIBRATION_RADIAL"],
                     "tangential_vibration": row["VIBRATION_TANGENTIAL"]}
        requests.post("http://127.0.0.1:7500/states", json=json_data)
        end = time.time()

        assert(end - start <= 0.2)

