import pytest
import requests


def test_login_successful():
    """
    Acceptance Testing 2.1
    Test that the user can successfully login with his correct phone number and password.
    """
    user_info = {"password": "abc123", "username": "0450539776",}
    response = requests.get("http://127.0.0.1:7700/login", params=user_info)
    assert(response.status_code == 200)
    assert("token" in response.json())


def test_invalid_phone_number():
    """
    Acceptance Testing 2.2
    Test that if the user’s phone number doesn’t exist, then red error message “Phone number doesn’t exist” should be displayed below the phone number field.
    """
    user_info = {"password": "acb123", "username": "413164212999",}
    response = requests.get("http://127.0.0.1:7700/login", params=user_info)
    assert(response.status_code == 403)
    assert("message" in response.json())
    assert(response.json()["message"] == "Invalid Username/Password")


def test_invalid_password():
    """
    Acceptance Testing 2.3
    Test that if the user’s password is incorrect, then red error message “Wrong password” should be displayed below the password field.
    """
    user_info = {"password": "hello", "username": "0450539776",}
    response = requests.get("http://127.0.0.1:7700/login", params=user_info)
    assert(response.status_code == 403)
    assert("message" in response.json())
    assert(response.json()["message"] == "Invalid Username/Password")


def test_page_redirection_after_successful_login():
    """
    Acceptance Testing 2.4
    Test that if it is a worker login, he will be leaded to a worker’s homepage and  if it is a manager login, he will be leaded to a manager’s homepage.
    """
    user_info = {"password": "abc123", "username": "0450539776",}
    response = requests.get("http://127.0.0.1:7700/login", params=user_info)
    assert(response.status_code == 200)
    assert("token" in response.json())
    assert """ Check web page is redirected to homepage. """
