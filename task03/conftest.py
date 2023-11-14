import pytest
from selenium import webdriver
from locators import BASE_URL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, timeout=12)
    return wait

def summa(num_1, num_2):
    return(int(num_1) + int(num_2))

