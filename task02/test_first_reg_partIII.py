import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

BASE_REG_URL = "http://suninjuly.github.io/registration1.html"
BASE_REG_URL_II = "http://suninjuly.github.io/registration2.html"

def test_first_element(driver):
    
    driver.get(BASE_REG_URL_II)

    time.sleep(2)

    first_name_field = driver.find_element(By.CSS_SELECTOR, '.first_block div:nth-child(1) input')
    first_name_field.send_keys('Ivan')

    last_name_field = driver.find_element(By.CSS_SELECTOR, '.first_block div:nth-child(2) input')
    last_name_field.send_keys('Golperin')
    
    email_field = driver.find_element(By.CSS_SELECTOR, '.first_block div:nth-child(3) input')
    email_field.send_keys('golperinIvan@gmail.com')
    
    button_field = driver.find_element(By.CSS_SELECTOR, 'button[type = "submit"]')
    button_field.click()

    time.sleep(2)
    message = driver.find_element(By.CSS_SELECTOR, 'h1')
    assert message.text == 'Congratulations! You have successfully registered!'
