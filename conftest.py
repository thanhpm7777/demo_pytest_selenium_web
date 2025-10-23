# conftest.py
import os
import csv
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def chrome_options():
    opts = Options()
    opts.set_capability("acceptInsecureCerts", True)
    opts.add_argument("--ignore-certificate-errors")
    # opts.add_argument("--headless=new")  # bật nếu muốn chạy headless
    return opts

@pytest.fixture(scope="function")
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def login_page(driver):
    return LoginPage(driver)
