import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data import DATA
import time

def test_switch_windows(driver, wait):

    #driver = webdriver.Chrome()
    driver.get(BASE_URL_SWITCH)

    driver.find_element(*FLY_BUTTON).click()
    
    window_names = driver.window_handles
    driver.switch_to.window(window_names[1])

    #или можно просто написать вот такое выражение для переключения на атоврое окно
    #driver.switch_to.window(driver.window_handles[1]) 
    
    num = driver.find_element(*VALUE_1).text
    driver.find_element(*FORM_FIELD_1).send_keys(calc(num))

    driver.find_element(*SUMBIT_BUT_1).click()

    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()
