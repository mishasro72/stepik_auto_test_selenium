from selenium.webdriver.common.by import By

BASE_URL = 'https://suninjuly.github.io/simple_form_find_task.html'

#form fields
FIRST_NAME = (By.CSS_SELECTOR,".form-control[name='first_name']")
LAST_NAME = (By. CSS_SELECTOR, ".form-control[name='last_name']")
CITY = (By.CSS_SELECTOR, ".city")
COUNTRY = (By.ID, "country")
BUTTON = (By.ID, "submit_button")



