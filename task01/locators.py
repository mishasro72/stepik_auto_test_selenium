from selenium.webdriver.common.by import By

BASE_URL = 'https://suninjuly.github.io/simple_form_find_task.html'
STEPIK_URL = 'https://stepik.org/'
STEPIK_SELENIUM_URL = 'https://stepik.org/lesson/138920/step/4?unit=196194'

#form fields
FIRST_NAME = (By.CSS_SELECTOR,".form-control[name='first_name']")
LAST_NAME = (By. CSS_SELECTOR, ".form-control[name='last_name']")
CITY = (By.CSS_SELECTOR, ".city")
COUNTRY = (By.ID, "country")
BUTTON = (By.ID, "submit_button")

#stepik
GET_IN = (By.CSS_SELECTOR, "#ember74")
LOGIN = (By.CSS_SELECTOR, "#id_login_email")
PASSWORD = (By.CSS_SELECTOR, "#id_login_password")
LOGIN_BUTTON = (By.XPATH, '//button[@class = "sign-form__btn button_with-loader "]')

ANSWER_FIELD = (By.CSS_SELECTOR, "ember879")
BUTTON_ANSWER = (By.CSS_SELECTOR, "//button[@class='submit-submission']")





