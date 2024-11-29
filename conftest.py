import pytest
from selenium import webdriver
from TestData import URLs


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(URLs.main_page_url)
    yield driver
    driver.quit()