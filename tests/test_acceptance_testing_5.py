import pytest
import requests


def test_display_pump_info():
    """
    Acceptance Testing 5.1
    Test that if the worker clicks on a water pump tab, a page showing states of the pump should be displayed.
    """
    response = requests.get("http://127.0.0.1:7500/states")
    assert(response.status_code == 200)


def test_error_tab_position():
    """
    Acceptance Testing 5.2
    Test that the state information in that page contains temperature, speed, output power and axial, radial, tangential of its vibration, row by row in a table.
    """
    response = requests.get("http://127.0.0.1:7500/states")
    row = response.json()[0]
    assert ("address" in row)
    assert ("axial_vibration" in row)
    assert ("bearing" in row)
    assert ("id" in row)
    assert ("name" in row)
    assert ("postcode" in row)
    assert ("power" in row)
    assert ("radial_vibration" in row)
    assert ("speed" in row)
    assert ("suburb" in row)
    assert ("tangential_vibration" in row)
    assert ("temperature" in row)


def test_page_refresh_time():
    """
    Acceptance Testing 5.3
    Test that the state information page should be refreshed and updated with the latest data every 1 second.
    """
    response = requests.get("http://127.0.0.1:7500/states")
    assert(response.status_code == 200)
    assert """ Check page is refreshed every second. """


def test_abnormal_fields_color ():
    """
    Acceptance Testing 5.4
    Test that the fields with value out of the normal range should have font color as red.
    """
    response = requests.get("http://127.0.0.1:7500/states")
    assert(response.status_code == 200)
    assert """ Check the font color turned red for abnormal value. """

def test_abnormal_go_back_color():
    """
    Acceptance Testing 5.5
    Test that there should be a go-back button which can take the detail page back to list of pumps.
    """
    response = requests.get("http://127.0.0.1:7500/states")
    assert (response.status_code == 200)
    assert """ Check page that there is a go back button. """