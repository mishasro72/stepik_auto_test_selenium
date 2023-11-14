import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data import DATA
import time

def test_file_send(driver, wait):

    #   driver = webdriver.Chrome()
    driver.get(BASE_URL_TEXT)

    driver.find_element(*FIRST_NAME).send_keys(DATA[0])
    driver.find_element(*LAST_NAME).send_keys(DATA[1])
    driver.find_element(*EMAIL).send_keys(DATA[2])

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    BUTTON = driver.find_element(*FILE)
    BUTTON.send_keys(file_path)
    #BUTTON.click()
    
   # time.sleep(1)
   # wait.until(EC.element_to_be_clickable(SUB_BUT)).click()
    driver.find_element(*SUB_BUT).click()

    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()
