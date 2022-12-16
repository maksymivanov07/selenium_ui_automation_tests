from selenium.webdriver.common.by import By

from selenium_tests.utilities.decorators import auto_step
from selenium_tests.utilities.web_ui.base_page import BasePage


@auto_step
class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __name_input = (By.XPATH, "//input[@name='REGISTER[NAME]']")
    __last_name_input = (By.XPATH, "//input[@name='REGISTER[LAST_NAME]']")
    __email_input = (By.XPATH, "//input[@name='REGISTER[EMAIL]']")
    __password_input = (By.XPATH, "//input[@name='REGISTER[PASSWORD]']")
    __confirm_password_input = (By.XPATH, "//input[@name='REGISTER[CONFIRM_PASSWORD]']")
    __telephone_number_input = (By.XPATH, "//input[@name='REGISTER[PHONE_NUMBER]']")
    __registrate_button = (By.XPATH, "//input[@value='Реєстрація']")
    __show_registration_form = (By.XPATH, "//header/div[1]/div[3]/a[2]")
    __click_contacts_page = (By.XPATH, "/html/body/header/div[1]/div[1]/nav/ul/li[8]/a")
    __click_phone_dropdown = (By.XPATH, "//button[@class='dropdown-toggle']")
    __error_name = (By.XPATH, "//label[@id='REGISTER[NAME]-error']")
    __error_last_name = (By.XPATH, "//label[@id='REGISTER[LAST_NAME]-error']")
    __error_email = (By.XPATH, "//label[@id='REGISTER[EMAIL]-error']")
    __error_password = (By.XPATH, "//label[@id='REGISTER[PASSWORD]-error']")
    __error_password_is_empty = (
    By.XPATH, "//label[@id='REGISTER[CONFIRM_PASSWORD]-error'][text()='Поле підтвердження паролю не заповнено']")
    __error_password_is_not_equal = (
    By.XPATH, "//label[@id='REGISTER[CONFIRM_PASSWORD]-error'][text()='Паролі не збігаються']")
    __error_phone_number = (By.XPATH, "//font[@class='errortext']")
    __logout_button = (By.XPATH, "//a[@href='/ua/?logout=yes']")

    def set_name(self, name):
        self._send_keys(self.__name_input, name)
        return self

    def set_last_name(self, last_name):
        self._send_keys(self.__last_name_input, last_name)
        return self

    def set_email(self, email):
        self._send_keys(self.__email_input, email)
        return self

    def set_password(self, password):
        self._send_keys(self.__password_input, password)
        return self

    def set_confirm_password(self, confirm_password):
        self._send_keys(self.__confirm_password_input, confirm_password)
        return self

    def set_phone_number(self, phone_number):
        self._send_keys(self.__telephone_number_input, phone_number)
        return self

    def is_error_name_visible(self):
        return self._is_visible(self.__error_name)

    def is_error_last_name_visible(self):
        return self._is_visible(self.__error_last_name)

    def is_error_email_visible(self):
        return self._is_visible(self.__error_email)

    def is_error_password_visible(self):
        return self._is_visible(self.__error_password)

    def is_error_is_empty_visible(self):
        return self._is_visible(self.__error_password_is_empty)

    def is_error_password_is_not_equal_visible(self):
        return self._is_visible(self.__error_password_is_not_equal)

    def is_error_phone_number_visible(self):
        return self._is_visible(self.__error_phone_number)

    def click_register(self):
        self._click(self.__registrate_button)
        return self

    def click_phone_dropdown(self):
        self._click(self.__click_phone_dropdown)
        return self

    def click_show_registration_form(self):
        self._click(self.__show_registration_form)
        return self

    def is_show_registration_form_visible(self):
        self._is_visible(self.__show_registration_form)
        return self

    def is_logout_button_visible(self):
        self._is_visible(self.__logout_button)
        return self
