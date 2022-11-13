import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


def test_loging():
    # auth test
    driver_chrome = Chrome('chromedriver')
    driver_chrome.get('https://authenticationtest.com/simpleFormAuth/')
    login = 'simpleForm@authenticationtest.com'
    password = 'pa$$w0rd'

    email_input_locator = "//input[@type='email']"
    time.sleep(3)
    email_input_element = driver_chrome.find_element(By.XPATH, email_input_locator)
    email_input_element.send_keys(login)
    time.sleep(3)

    password_input_locator = "//input[@type='password']"
    time.sleep(3)
    password_input_element = driver_chrome.find_element(By.XPATH, password_input_locator)
    password_input_element.send_keys(password)
    time.sleep(3)

    button_login_locator = "//input[@type='submit']"
    time.sleep(3)
    button_input_element = driver_chrome.find_element(By.XPATH, button_login_locator)
    button_input_element.click()
    time.sleep(3)

    driver_chrome.quit()
