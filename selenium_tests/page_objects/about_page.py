from selenium.webdriver.common.by import By

from selenium_tests.utilities.web_ui.base_page import BasePage


class AboutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __click_contacts_page = (By.XPATH, "//div[@class='header_top wrap']/div/nav/ul/li[8]/a")
    __name_input = (By.XPATH, "//input[@name='user_name']")
    __email_input = (By.XPATH, "//input[@id='user_email']")
    __message_input = (By.XPATH, "//textarea[@name='MESSAGE']")
    __click_submit_button = (By.XPATH, "//div[@id='comp_7f208c379468439f140b97772ac3b622']//button")
    __error_name = (By.XPATH, "//div[@id='comp_7f208c379468439f140b97772ac3b622']/p[1]/*")
    __error_email = (By.XPATH, "//div[@id='comp_7f208c379468439f140b97772ac3b622']/p[2]/*")
    __error_message = (By.XPATH, "//div[@id='comp_7f208c379468439f140b97772ac3b622']/p[3]/*")
    __error_wrong_email = (By.XPATH, "//div[@id='comp_7f208c379468439f140b97772ac3b622']/p[2]/*")
    __error_captcha = (By.XPATH, "//div[@id='comp_7f208c379468439f140b97772ac3b622']/p[4]/*")
    __phone_number = (By.XPATH, "//div[@class='address_cont-page']/div/a")

    def click_contacts_page(self):
        self._click(self.__click_contacts_page)
        return self

    def set_name(self, name):
        self._send_keys(self.__name_input, name)
        return self

    def set_email(self, email):
        self._send_keys(self.__email_input, email)
        return self

    def set_message(self, message):
        self._send_keys(self.__message_input, message)
        return self

    def click_submit_button(self):
        self._click(self.__click_submit_button)
        return self

    def is_phone_number_clickable(self):
        return self._clickable(self.__phone_number)

    def is_error_name_visible(self):
        return self._is_visible(self.__error_name)

    def is_error_email_visible(self):
        return self._is_visible(self.__error_email)

    def is_error_wrong_email_visible(self):
        return self._is_visible(self.__error_wrong_email)

    def is_error_message_visible(self):
        return self._is_visible(self.__error_message)

    def is_error_captcha_visible(self):
        return self._is_visible(self.__error_captcha)
