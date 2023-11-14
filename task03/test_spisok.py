import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from locators import *
import time


def test_spisok(driver, wait):

    driver.get(BASE_URL)

    #создаем класс Select и передаем значение раскрывающегося списка
    dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#dropdown"))

    #считаем сумму числе используя функцию summa которую мы прописали в locators
    answer = summa(driver.find_element(*NUM_1).text, driver.find_element(*NUM_2).text)

    #выбираем пункт меню со значнеием полученной суммы
    dropdown.select_by_value(str(answer))

    #для информации перчаем пукт меню, который мы выбрали
    selected_option = dropdown.first_selected_option.text
    print(selected_option)

    #кликаемпо кнопке submit
    driver.find_element(*SUMBIT).click()

    # в появившемся алерте получаем тект сообщения и выводим его на печать
    alert = wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()
