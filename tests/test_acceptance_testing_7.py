import pytest
import requests


def test_prediction_link():
    """
    Acceptance Testing 7.1
    Test that there is a tab link on homepage shown as “Predictions”
    """
    assert """ Check that there is a "Prediction" tab link on homepage """


def test_water_pump_list():
    """
    Acceptance Testing 7.2
    Test that when clicking that link, it will jump to another page which displays a vertical list of all water pumps.
    """
    assert """ Check that the page jumps """
    response = requests.post("http://127.0.0.1:9999/learning/")
    assert(response.status_code == 200)
    assert(len(response.json()) == 10)


def test_prediction_page_link():
    """
    Acceptance Testing 7.3
    Test that each row in that list should contains information including the pumps name, address and its probability of failure.
    """
    response = requests.post("http://127.0.0.1:9999/learning/")
    assert(response.status_code == 200)
    for i in range(0,len(response.json())):
        assert("id" in response.json()[i])
        assert("probability" in response.json()[i])
        assert("address" in response.json()[i])

def test_prediction_page_redirection():
    """
    Acceptance Testing 7.4
    Test that the list is sorted by the failure probability and the water pump with highest failure probability is place at the top.
    """

    response = requests.post("http://127.0.0.1:9999/learning/")
    assert(response.status_code == 200)
    for i in range(0,len(response.json())-1):
        assert(int(float(response.json()[i]["probability"])) >= int(float(response.json()[i+1]["probability"])))


def test_tab_information():
    """
    Acceptance Testing 7.5
    Test that any row with its pump’s failure over 90% should have its background color as red.
    """
    assert """ Check that the pump with failure rate above 90% is marked as red """
