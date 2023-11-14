import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data import DATA
import time

def test_alerts(driver, wait):

    #driver = webdriver.Chrome()
    driver.get(BASE_URL_ALERT)
    window_name = driver.window_handles
    print(window_name)
    
    driver.switch_to.window(window_name[0])
    driver.find_element(*JOIN_BITTON).click()
    #print(driver.window_handles)

    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    number = driver.find_element(*VALUE)
    answer = calc(number.text)
    #print(answer)

    # window_name = driver.window_handles
    # print(window_name)

    driver.find_element(*FORM_FIELD).send_keys(answer)
    driver.find_element(*JOIN_BITTON).click()
    time.sleep(2)

    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()






