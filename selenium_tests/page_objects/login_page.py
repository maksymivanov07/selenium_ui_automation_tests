from selenium.webdriver.common.by import By

from selenium_tests.page_objects.home_page import HomePage
from selenium_tests.utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __show_login_form = (By.XPATH, "//header/div[1]/div[3]/a/span[2]")
    __email_input = (By.XPATH, "//input[@name='USER_LOGIN']")
    __password_input = (By.XPATH, "//input[@name='USER_PASSWORD']")
    __login_button = (By.XPATH, "//input[@name='Login']")
    __forgot_password_button = (By.XPATH, "//a[@class='forgot-password']")
    __error_email = (By.XPATH, "//label[@for='USER_LOGIN']")
    __error_password = (By.XPATH, "//label[@for='USER_PASSWORD']")
    __error_login = (By.XPATH, "//div[@style='color: red;']")
    __sent_button = (By.XPATH, "//input[@name='send_account_info']")
    __profile_button = (By.XPATH, "//header/div[1]/div[3]/a[1]/span[2]/div")

    def set_auth_email(self, email):
        self._send_keys(self.__email_input, email)
        return self

    def set_auth_password(self, password):
        self._send_keys(self.__password_input, password)
        return self

    def is_error_email_visible(self):
        return self._is_visible(self.__error_email)

    def is_error_password_visible(self):
        return self._is_visible(self.__error_password)

    def is_error_login_visible(self):
        return self._is_visible(self.__error_login)

    def is_sent_button_visible(self):
        return self._is_visible(self.__sent_button)

    def is_login_button_visible(self):
        return self._is_visible(self.__login_button)

    def click_forgot_password(self):
        self._click(self.__forgot_password_button)
        return self

    def click_show_login_form(self):
        self._click(self.__show_login_form)
        return self

    def click_show_user_profile(self):
        self._click(self.__profile_button)
        return self

    def click_login(self):
        self._click(self.__login_button)
        return self

    def login(self, email, password):
        self.set_auth_email(email).set_auth_password(password).click_login()
        return HomePage(self._driver)

