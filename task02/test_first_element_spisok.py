import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data import *
import time

def test_first_element(driver, wait):
    
    #driver = webdriver.Chrome()
    driver.get(BASE_REG_URL)

    first_name_field = wait.until(EC.visibility_of_any_elements_located(FIRST_BLOCK_ELEM))
    i = 0
    for element in first_name_field:
        element.send_keys(DATA_FISRT_BLOCK[i])
        i += 1

    button_field = wait.until(EC.element_to_be_clickable(SUB_FIRST_BUT))
    button_field.click()

    message = wait.until(EC.visibility_of_element_located(REG_MESSAGE))
    assert message.text == 'Congratulations! You have successfully registered!'
