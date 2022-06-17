__author__ = 'miserylab'

import chromedriver_autoinstaller
import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session", autouse=True)
def set_web_driver():
    s = chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(service=Service(s))
    browser.set_driver(driver)