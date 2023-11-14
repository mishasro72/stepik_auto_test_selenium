import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data import *
import time


def test_checkbox(driver, wait):
    
    #driver = webdriver.Chrome()
    driver.get(BASE_URL_MATH)

    x = driver.find_element(*x_field).text

    x = calc(x)
    answer_field = wait.until(EC.visibility_of_element_located(ANSWER))
    answer_field.send_keys(x)

    wait.until(EC.visibility_of_element_located(CHECKBOX)).click()
    wait.until(EC.visibility_of_element_located(RADIO_BUTTON)).click()

    button_field = wait.until(EC.element_to_be_clickable(SUM_MIT))
    button_field.click()

    alert = wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert

    print(alert.text)
    alert.accept()
    