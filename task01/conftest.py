import pytest
from selenium import webdriver
from locators import BASE_URL
from selenium.webdriver.support.wait import WebDriverWait






@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait


