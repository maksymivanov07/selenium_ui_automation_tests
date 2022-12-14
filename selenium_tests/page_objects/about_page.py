from selenium.webdriver.common.by import By

from selenium_tests.utilities.decorators import auto_step
from selenium_tests.utilities.web_ui.base_page import BasePage


@auto_step
class AboutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __name_input = (By.XPATH, "//input[@name='user_name']")
    __email_input = (By.XPATH, "//input[@id='user_email']")
    __message_input = (By.XPATH, "//textarea[@name='MESSAGE']")
    __click_submit_button = (By.XPATH, "//div[@id='comp_7f208c379468439f140b97772ac3b622']//button")
    __error_name = (By.XPATH, "//div[@id='comp_7f208c379468439f140b97772ac3b622']/p[1]/*")
    __error_email = (By.XPATH, "//div[@id='comp_7f208c379468439f140b97772ac3b622']/p[2]/*")
    __error_message = (By.XPATH, "//div[@id='comp_7f208c379468439f140b97772ac3b622']/p[3]/*")
    __error_wrong_email = (By.XPATH, "//div[@id='comp_7f208c379468439f140b97772ac3b622']/p[2]/*")
    __error_captcha = (By.XPATH, "//div[@id='comp_7f208c379468439f140b97772ac3b622']/p[4]/*")
    __error_captcha_single = (By.XPATH, "//div[@id='comp_7f208c379468439f140b97772ac3b622']/p[1]/*")
    __phone_number = (By.XPATH, "//div[@class='address_cont-page']/div/a")

    def set_name(self, name):
        """
        Set name in field name
        :param name: name
        :return: self
        """
        self._send_keys(self.__name_input, name)
        return self

    def set_email(self, email):
        """
         Set name in field email
         :param name: email
         :return: self
         """
        self._send_keys(self.__email_input, email)
        return self

    def set_message(self, message):
        """
         Set message in field name
         :param name: message
         :return: self
         """
        self._send_keys(self.__message_input, message)
        return self

    def click_submit_button(self):
        """
        Click on button sumbit page
        :return: self
        """
        self._click(self.__click_submit_button)
        return self

    def is_phone_number_clickable(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._clickable(self.__phone_number)

    def is_error_name_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__error_name)

    def is_error_email_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__error_email)

    def is_error_wrong_email_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__error_wrong_email)

    def is_error_message_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__error_message)

    def is_error_captcha_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__error_captcha)

    def is_error_captcha_single_position_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__error_captcha_single)
