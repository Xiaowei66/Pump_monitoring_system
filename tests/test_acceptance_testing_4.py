import requests


def test_error_tab_color():
    """
    Acceptance Testing 4.1
    Test that if server receives abnormal data from any sensor, the related water pump’s corresponding tab should have its background color as red.
    """
    response = requests.get("http://127.0.0.1:8500/status")
    assert(response.status_code == 200)
    for i in range(0,len(response.json())):
        if response.json()[i]["error"]=="Abnormal" :
            assert(i==0)
            break

def test_error_tab_position():
    """
    Acceptance Testing 4.2
    Test that if server receives abnormal data from any sensor, the related water pump’s corresponding tab should be placed at the top.
    """
    response = requests.get("http://127.0.0.1:8500/status")
    assert(response.status_code == 200)
    for i in range(0,len(response.json())):
        if response.json()[i]["error"]=="Abnormal" :
            assert(i==0)
            break

def test_error_tab_returns_normal():
    """
    Acceptance Testing 4.3
    Test that if the abnormal fields of data received by the server return to normal, the corresponding red tabs should turn back white and moved down from the top of list.
    """
    response = requests.get("http://127.0.0.1:8500/status")
    assert(response.status_code == 200)
    for i in range(0,len(response.json())):
        if response.json()[i]["error"]=="Abnormal" :
            assert(i==0)
            break
