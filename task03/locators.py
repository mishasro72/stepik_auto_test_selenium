from selenium.webdriver.common.by import By
import math


def summa(num_1, num_2):
    return(int(num_1) + int(num_2))

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

BASE_URL = "https://suninjuly.github.io/selects1.html"
BASE_URL_SCROLL = "https://SunInJuly.github.io/execute_script.html"

#для задания по рвыпадающим спискам
NUM_1 = (By.CSS_SELECTOR, "#num1")
NUM_2 = (By.CSS_SELECTOR, "#num2")
SUMBIT = (By.CSS_SELECTOR, "button[type = 'submit']")

#  для задания по скроллу страницы используя java script
NUM = (By.CSS_SELECTOR, "#input_value")
ANSWER_FIELD = (By.CSS_SELECTOR, "#answer")
ROBO_CHECK = (By.CSS_SELECTOR, "#robotCheckbox")
ROBO_RUL = (By.CSS_SELECTOR, "#robotsRule")
SUMBIT_BUT = (By.CSS_SELECTOR, "button[type='submit']")

#для задания по отправки файла в форму
BASE_URL_TEXT = "http://suninjuly.github.io/file_input.html"
FIRST_NAME = (By.CSS_SELECTOR, "input[name='firstname']")
LAST_NAME = (By.CSS_SELECTOR, "input[name='lastname']")
EMAIL = (By.CSS_SELECTOR, "input[name='email']")
FILE = (By.CSS_SELECTOR, "#file")
SUB_BUT = (By.CSS_SELECTOR, "button[type='submit']")

#для задания с алертами
BASE_URL_ALERT = "http://suninjuly.github.io/alert_accept.html"
JOIN_BITTON = (By.CSS_SELECTOR, "button[type='submit']")
VALUE = (By.ID, 'input_value')
FORM_FIELD = (By.ID, 'answer')

#для переключения между окнами
BASE_URL_SWITCH = " http://suninjuly.github.io/redirect_accept.html"
FLY_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
VALUE_1 = (By.ID, 'input_value')
FORM_FIELD_1 = (By.ID, 'answer')
SUMBIT_BUT_1 = (By.CSS_SELECTOR, "button[type='submit']")

#для бронировани янужной цены 
BASE_URL_BOOK = "http://suninjuly.github.io/explicit_wait2.html"
PRICE = (By.ID, "price")
BOOK_BUTTON = (By.ID, "book")
VALUE_2 = (By.ID, "input_value")
FORM_FIELD_2 = (By.ID, 'answer')
SUBMIT_BOOK = (By.ID, "solve")







