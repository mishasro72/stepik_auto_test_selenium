import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data import *
import time

def test_form(driver, wait):

    #driver = webdriver.Chrome()

    driver.get(BASE_URL)
    first_name_field = driver.find_element(*FIRST_NAME)
    first_name_field.send_keys(F_NAME)
    assert first_name_field.get_attribute('value') == F_NAME

    last_name_field = driver.find_element(*LAST_NAME)
    last_name_field.send_keys(L_NAME)
    assert last_name_field.get_attribute('value') == L_NAME

    city_field = driver.find_element(*CITY)
    city_field.send_keys(CITY_CUR)
    assert city_field.get_attribute('value') == CITY_CUR

    country_field = driver.find_element(*COUNTRY)
    country_field.send_keys(COUNTRY_CUR)
    assert country_field.get_attribute('value') == COUNTRY_CUR

    button_field = driver.find_element(*BUTTON)
    button_field.click()
    
    time.sleep(3)
    alert = driver.switch_to.alert
    text = alert.text
    password = ""
    for i in text:
        if i.isdigit() or i == ".":
            password += i
    print(password)
    alert.accept()
    driver.switch_to.default_content
    #time.sleep(2)
    
    #переходим на сайт stepik
    # driver.get('https://stepik.org/')
    # BUT = wait.until(EC.element_to_be_clickable(GET_IN))
    # time.sleep(2)
    # BUT.click()
    





    





