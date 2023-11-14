import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data import *
import time

def test_form(driver):
    
    driver = webdriver.Chrome()
    driver.get(BASE_URL_HUGE)

    elements_fields = driver.find_elements(*ELEMENTS_FIELDS)

    for element in elements_fields:
        element.send_keys("Данные")
    SUBMIT_BUT = driver.find_element(*SUBMIT_BUTTON).click()
    
    time.sleep(3)
    alert = driver.switch_to.alert
    text = alert.text
    password = ""
    for i in text:
        if i.isdigit() or i == ".":
            password += i
    print(password)

