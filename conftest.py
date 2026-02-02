import pytest
from selenium import webdriver
from data import URL

@pytest.fixture
def driver():
    url = URL().base_url
    driver = webdriver.Chrome()
    driver.get(url)
    yield driver
