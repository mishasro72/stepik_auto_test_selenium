from selenium import webdriver
from selenium.webdriver.common.by import By

def test_java_script():
    driver = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    driver.get(link)
    button = driver.find_element(By.TAG_NAME, "button")
    driver.execute_script("window.scrollBy(0, 100);")
    button.click()
