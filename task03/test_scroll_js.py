import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from locators import *
import time


def test_scroll_js(driver, wait):

   # driver = webdriver.Chrome()
    driver.get(BASE_URL_SCROLL)

    number = driver.find_element(*NUM)
    answer = calc(number.text)
    driver.find_element(*ANSWER_FIELD).send_keys(answer)

    driver.find_element(*ROBO_CHECK).click()
    
    driver.execute_script("window.scrollBy(0, 350);")
    driver.find_element(*ROBO_RUL).click()


    driver.find_element(*SUMBIT_BUT).click()


    time.sleep(2)

    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()
