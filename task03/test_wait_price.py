import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data import *
import time

def test_wait_price(driver, wait):

    driver = webdriver.Chrome()
    driver.get(BASE_URL_BOOK)

    # style = driver.find_element(By.CSS_SELECTOR, "div[class='card']")
    # print(f"\n{style.get_attribute('style')}")

    time.sleep(12)
    button = driver.find_element(By.ID, "book")
    print(f"\n{button.get_attribute('disabled')}")
    # wait.until(EC.text_to_be_present_in_element((PRICE), '100'))
    # driver.find_element(*BOOK_BUTTON).click()

    # number = wait.until(EC.visibility_of_element_located(VALUE_2)).text
    # answer = calc(number)

    # wait.until(EC.visibility_of_element_located(FORM_FIELD_2)).send_keys(answer)
    
    # wait.until(EC.element_to_be_clickable(SUBMIT_BOOK)).click()

    # wait.until(EC.alert_is_present())
    # alert = driver.switch_to.alert
    # print(alert.text)
    # alert.accept()






