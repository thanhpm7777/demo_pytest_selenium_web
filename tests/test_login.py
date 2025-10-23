import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_page_loads(login_page):
    login_page.open_page()
    assert (login_page.username_field().is_displayed() and
            login_page.pass_field().is_displayed() and
            login_page.button_sign_in().is_displayed())

def test_successful_login(login_page):

    login_page.login_page(username="Pham", password="123456")
    assert not login_page.is_logout_displayed()

def test_invalid_login(login_page):

    login_page.login_page(username="Pham", password="wrongpass")
    error_msg = login_page.get_error_message()
    assert "Incorrect credentials" in error_msg, f" Unexpected error message: {error_msg}"


def test_ui_login(login_page):
    login_page.open_page()
    assert login_page.forgot_visible()
    login_page.login_page(username="", password="")
    assert login_page.is_sign_in_disabled()

def test_security_pass(login_page):
    login_page.open_page()
    login_page.enter_password("abc123")
    assert login_page.is_password_masked()
