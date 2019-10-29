import requests
import pytest

def test_each_tab_information():
    """
    Acceptance Testing 3.1
    Test that each tab should correctly show its pump’s name and address on it.
    """
    response = requests.get("http://127.0.0.1:8500/status")
    assert(response.status_code == 200)
    for i in range(0,len(response.json())):
        assert("id" in response.json()[i])
        assert("error" in response.json()[i])
        assert("address" in response.json()[i])

def test_name_address_position():
    """
    Acceptance Testing 3.2
    Test that name is shown in the first column on tab, while address is shown in the second column.
    """
    response = requests.get("http://127.0.0.1:8500/status")
    assert(response.status_code == 200)
    assert("id" in response.json()[0])
    assert("error" in response.json()[0])
    assert("address" in response.json()[0])


def test_all_pumps_included():
    """
    Acceptance Testing 3.3
    Test that all pumps are included in the list.
    """
    response = requests.get("http://127.0.0.1:8500/status")
    assert(response.status_code == 200)
    assert(len(response.json()) == 10)

