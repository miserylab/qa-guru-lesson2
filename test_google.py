__author__ = 'miserylab'

from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture()
def open_google():
    browser.open('https://google.com')


@pytest.fixture()
def insert_selene():
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()


@pytest.fixture(scope='session', autouse=True)
def init_browser():
    browser.config.window_width = 1200
    browser.config.window_height = 1000


def test_first(open_google, insert_selene):
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_negative(open_google, insert_selene):
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))