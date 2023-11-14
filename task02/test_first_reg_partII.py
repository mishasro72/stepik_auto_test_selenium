import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from locators import *
# from data import *
# import time

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait

BASE_REG_URL = "http://suninjuly.github.io/registration1.html"
BASE_REG_URL_II = "http://suninjuly.github.io/registration2.html"

def test_first_element(driver, wait):
    
    driver.get(BASE_REG_URL_II)

    first_name_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.first_block div:nth-child(1) input')))
    first_name_field.send_keys('Ivan')

    last_name_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.first_block div:nth-child(2) input')))
    last_name_field.send_keys('Golperin')
    
    email_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.first_block div:nth-child(3) input')))
    email_field.send_keys('golperinIvan@gmail.com')
    
    button_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type = "submit"]')))
    button_field.click()

    message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1')))
    assert message.text == 'Congratulations! You have successfully registered!'
