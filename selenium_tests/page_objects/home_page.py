from selenium.webdriver.common.by import By

from selenium_tests.utilities.decorators import auto_step
from selenium_tests.utilities.web_ui.base_page import BasePage
from selenium_tests.page_objects.about_page import AboutPage
from selenium_tests.page_objects.login_page import LoginPage
from selenium_tests.page_objects.checkout_page import CheckoutPage
from selenium_tests.page_objects.user_profile_page import UserProfilePage


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
    __registrate_button = (By.XPATH, "//div[@class='row buttons clearfix']//input")
    __show_registration_form = (By.XPATH, "//div[@class='header_top wrap']//div[@class='user-login']//a[2]")
    __logout_button = (By.XPATH, "//div[@class='header_top wrap']//div[@class='user-login']/a[2]")
    __click_contacts_page = (By.XPATH, "//div[@class='header_top wrap']//li[8]/a")
    __click_phone_dropdown = (By.XPATH, "//button[@class='dropdown-toggle']")
    __additional_phone = (By.XPATH, "//ul[@class='dropdown-menu show']//li[2]/a")
    __error_name = (By.XPATH, "//label[@id='REGISTER[NAME]-error']")
    __error_last_name = (By.XPATH, "//label[@id='REGISTER[LAST_NAME]-error']")
    __error_email = (By.XPATH, "//label[@id='REGISTER[EMAIL]-error']")
    __error_password = (By.XPATH, "//label[@id='REGISTER[PASSWORD]-error']")
    __error_phone_number = (By.XPATH, "//font[@class='errortext']")
    __show_login_form = (By.XPATH, "//header/div[1]/div[3]/a/span[2]")
    __click_item = (By.XPATH, "//div[@class='new-items-content catalog-lvl2']/div[1]")
    __click_cart_on_item = (By.XPATH, "//div[@class='new-items-content catalog-lvl2']/div[1]//div[@class='bottom']")
    __cart_button = (By.XPATH, "//*[@id='shopping-cart_4_']")
    __profile_button = (By.XPATH, "//div[@class='header_top wrap']//div[@class='user-login']//div")
    __favorite_button = (By.XPATH, "//a[@id='want']")

    def click_item(self):
        """
        Wait for element and click when it would visible
        :return: self
        """
        self._click(self.__click_item)
        return CheckoutPage(self._driver)

    def click_cart_on_item(self):
        """
        Wait for element and click when it would visible
        :return: self
        """
        self._click(self.__click_cart_on_item)
        return CheckoutPage(self._driver)

    def click_cart_button(self):
        """
        Wait for element and click when it would visible
        :return: self
        """
        self._click(self.__cart_button)
        return CheckoutPage(self._driver)

    def click_contacts_page(self):
        """
        Wait for element and click when it would visible
        :return: self
        """
        self._click(self.__click_contacts_page)
        return AboutPage(self._driver)

    def click_show_login_form(self):
        """
        Wait for element and click when it would visible
        :return: self
        """
        self._click(self.__show_login_form)
        return LoginPage(self._driver)

    def click_register(self):
        """
        Wait for element and click when it would visible
        :return: self

        """
        self._click(self.__registrate_button)
        return HomePage(self._driver)

    def click_show_user_profile(self):
        """
        Wait for element and click when it would visible
        :return: self
        """
        self._click(self.__profile_button)
        return UserProfilePage(self._driver)

    def click_favorite_button(self):
        """
        Wait for element and click when it would visible
        :return: self
        """
        self._click(self.__favorite_button)
        return UserProfilePage(self._driver)

    def click_show_registration_form(self):
        """
        Wait for element and click when it would visible
        :return: self
        """
        self._click(self.__show_registration_form)
        return self

    def click_phone_dropdown(self):
        """
        Wait for element and click when it would visible
        :return: self
        """
        self._click(self.__click_phone_dropdown)
        return self

    def set_name(self, name):
        """
        Set name in field name
        :param name: name
        :return: self
        """
        self._send_keys(self.__name_input, name)
        return self

    def set_last_name(self, last_name):
        """
        Set name in field last name
        :param last_name: last name
        :return: self
        """
        self._send_keys(self.__last_name_input, last_name)
        return self

    def set_email(self, email):
        """
        Set name in field email
        :param email: email
        :return: self
        """
        self._send_keys(self.__email_input, email)
        return self

    def set_password(self, password):
        """
        Set name in field passwrod
        :param password: password
        :return: self
        """
        self._send_keys(self.__password_input, password)
        return self

    def set_confirm_password(self, confirm_password):
        """
        Set name in field confirm_password
        :param confirm_password: confirm_password
        :return: self
        """
        self._send_keys(self.__confirm_password_input, confirm_password)
        return self

    def set_phone_number(self, phone_number):
        """
        Set name in field phone_number
        :param phone_number: phone_number
        :return: self
        """
        self._send_keys(self.__telephone_number_input, phone_number)
        return self

    def is_error_name_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__error_name)

    def is_error_last_name_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__error_last_name)

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

    def is_error_is_empty_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__error_password)

    def is_error_password_is_not_equal_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__error_password)

    def is_error_phone_number_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__error_phone_number)

    def is_show_registration_form_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        self._is_visible(self.__show_registration_form)
        return self

    def is_additional_number_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__additional_phone)

    def is_logout_button_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__logout_button)

