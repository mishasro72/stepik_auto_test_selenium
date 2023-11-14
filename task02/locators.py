from selenium.webdriver.common.by import By
import math

# BASE_URL = "https://www.degreesymbol.net/"
# DEGREE_IN_MATH = "Degree Symbol in Math"
# MATH = "Math"

BASE_URL = "http://suninjuly.github.io/find_link_text"
BASE_URL_HUGE = "http://suninjuly.github.io/huge_form.html"
TEXT_LINK = str(math.ceil(math.pow(math.pi, math.e)*10000))
#print(TEXT_LINK)

BASE_REG_URL = "http://suninjuly.github.io/registration1.html"
BASE_REG_URL_II = "http://suninjuly.github.io/registration2.html"

BASE_URL_MATH = "https://suninjuly.github.io/math.html"

BASE_URL_ATTRIBUTE = "https://suninjuly.github.io/get_attribute.html"

#form fields
FIRST_NAME = (By.CSS_SELECTOR,".form-control[name='first_name']")
LAST_NAME = (By. CSS_SELECTOR, ".form-control[name='last_name']")
CITY = (By.CSS_SELECTOR, ".city")
COUNTRY = (By.ID, "country")
BUTTON = (By.XPATH, "//button[@class='btn btn-default']")

#for huge form
ELEMENTS_FIELDS = (By.XPATH, "//input[@type='text']")
SUBMIT_BUTTON = (By.XPATH, "//button[@class='btn btn-default']")

#for XPATH search
BASE_XPATH_URL = "http://suninjuly.github.io/find_xpath_form"
SUB_BUT_XPATH = (By.XPATH, "//button[@type='submit']")
ELEM_FIELDS_XPATH = (By.XPATH, "//input[@type='text']")

#for registration testing
FIRST_BLOCK_ELEM = (By.CSS_SELECTOR, "div[class='first_block'] input")
SUB_FIRST_BUT = (By.CSS_SELECTOR, 'button[type = "submit"]')
REG_MESSAGE = (By.CSS_SELECTOR, 'h1')


#for math opage

x_field = (By.CSS_SELECTOR, "#input_value")
ANSWER = (By.CSS_SELECTOR, "#answer")
CHECKBOX = (By.CSS_SELECTOR, "#robotCheckbox")
RADIO_BUTTON = (By.CSS_SELECTOR, "#robotsRule")
SUM_MIT = (By.CSS_SELECTOR, "button[type ='submit']")


#for get_attribute

TRESURE = (By.CSS_SELECTOR, "#treasure")
ANSWER = (By.CSS_SELECTOR, "#answer")
CHECKBOX = (By.CSS_SELECTOR, "#robotCheckbox")
RADIO_BUTTON = (By.CSS_SELECTOR, "#robotsRule")
SUM_MIT = (By.CSS_SELECTOR, "button[type ='submit']")




