import pytest
import requests


def test_sensor_abnormal_satus():
    """
    Acceptance Testing 8.1
    Test that if server receives abnormal data from any sensor, the workers should receive the SMS alert within 2 seconds.
    """
    json_data = {"id": 7037,
                 "bearing": 1,
                 "temperature": 60,
                 "speed": 1492.3433,
                 "power": 177.3134,
                 "axial_vibration": 0.0383,
                 "radial_vibration": 0.0383,
                 "tangential_vibration": 0.0383}
    requests.post("http://127.0.0.1:7500/states", json=json_data)
    assert """ Check phone receives message """


def test_predicted_abnormal_satus():
    """
    Acceptance Testing 8.2
    Test that if a water pump has a failure probability over 90% the workers should receive the SMS alert in 2 seconds.
    """
    json_data = {"id": 7037,
                 "bearing": 1,
                 "temperature": 60,
                 "speed": 1492.3433,
                 "power": 177.3134,
                 "axial_vibration": 0.0383,
                 "radial_vibration": 0.0383,
                 "tangential_vibration": 0.0383}
    requests.post("http://127.0.0.1:7500/states", json=json_data)
    assert """ Check phone receives message """

def test_sms_information():
    """
    Acceptance Testing 8.3
    Test that the SMS alert sent should contain the fault pump’s name, address and abnormal state factor (e.g. “temperature”, “speed” or the string “predicted” if it’s from the  machine learning module)
    """
    json_data = {"id": 7037,
                 "bearing": 1,
                 "temperature": 60,
                 "speed": 1492.3433,
                 "power": 177.3134,
                 "axial_vibration": 0.0383,
                 "radial_vibration": 0.0383,
                 "tangential_vibration": 0.0383}
    requests.post("http://127.0.0.1:7500/states", json=json_data)
    assert """ Check phone message information """
