from selenium.webdriver.common.by import By

from selenium_tests.utilities.decorators import auto_step
from selenium_tests.utilities.web_ui.base_page import BasePage


@auto_step
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __login_button = (By.XPATH, "//input[@name='Login']")
    __email_input = (By.XPATH, "//input[@name='USER_LOGIN']")
    __password_input = (By.XPATH, "//input[@name='USER_PASSWORD']")
    __forgot_password_button = (By.XPATH, "//a[@class='forgot-password']")
    __error_email = (By.XPATH, "//label[@for='USER_LOGIN']")
    __error_password = (By.XPATH, "//label[@for='USER_PASSWORD']")
    __error_login = (By.XPATH, "//div[@style='color: red;']")
    __error_user_not_found = (By.XPATH, "//font[@class='errortext']")
    __email_field = (By.XPATH, "//input[@name='USER_EMAIL']")
    __button_send = (By.XPATH, "//input[@name='send_account_info']")

    def set_auth_email(self, email):
        """
        Set name in field email
        :param email: email
        :return: self
        """
        self._send_keys(self.__email_input, email)
        return self

    def set_forgott_password_email(self, email):
        """
        Set name in field email
        :param email: email
        :return: self
        """
        self._send_keys(self.__email_field, email)
        return self

    def set_auth_password(self, password):
        """
        Set name in field password
        :param password: password
        :return: self
        """
        self._send_keys(self.__password_input, password)
        return self

    def is_error_email_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__error_email)

    def is_error_password_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__error_password)

    def is_error_login_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__error_login)

    def is_login_button_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__login_button)

    def is_error_user_not_found_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__error_user_not_found)

    def click_forgot_password(self):
        """
        Wait for element and click when it would visible
        :return: self
        """
        self._click(self.__forgot_password_button)
        return self

    def click_send_email(self):
        """
        Wait for element and click when it would visible
        :return: self
        """
        self._click(self.__button_send)
        return self

    def click_login(self):
        """
        Wait for element and click when it would visible
        :return: self
        """
        self._click(self.__login_button)
        return self

