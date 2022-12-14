from selenium.webdriver.common.by import By

from selenium_tests.utilities.decorators import auto_step
from selenium_tests.utilities.web_ui.base_page import BasePage


@auto_step
class UserProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __click_edit_profile = (By.XPATH, "//a[@class='btn edit_profile']")
    __name_input = (By.XPATH, "//input[@id='nameLk1']")
    __last_name_input = (By.XPATH, "//input[@id='LAST_NAME']")
    __surname_input = (By.XPATH, "//input[@id='SECOND_NAME']")
    __email_input = (By.XPATH, "//input[@id='EMAIL']")
    __subscription_email_input = (By.XPATH, "//input[@id='EMAIL']")
    __login_input = (By.XPATH, "//input[@id='LOGIN']")
    __new_pass_input = (By.XPATH, "//input[@name='NEW_PASSWORD']")
    __old_pass_input = (By.XPATH, "//input[@name='NEW_PASSWORD_CONFIRM']")
    __button_save = (By.XPATH, "//input[@name='save']")
    __button_subscription_ok = (By.XPATH, "//input[@value='ок']")
    __button_sent_confirmation_code = (By.XPATH, "//div[@class='subscription-utility']//input[@type='submit']")
    __button_subscription_submit = (By.XPATH, "//input[@name='Save']")
    __subscription_positive = (By.XPATH, "//font[@class='notetext']")
    __subscription_error = (By.XPATH, "//font[@class='errortext']")

    def click_contacts_page(self):
        """
        Click on button contacts page
        :return: self
        """
        self._click(self.__click_edit_profile)
        return self

    def click_button_save(self):
        """
        Click on button contacts page
        :return: self
        """
        self._click(self.__button_save)
        return self

    def click_button_subscription_submit(self):
        """
        Click on button contacts page
        :return: self
        """
        self._click(self.__button_subscription_submit)
        return self

    def click_button_sent_confirmation_code(self):
        """
        Click on button contacts page
        :return: self
        """
        self._click(self.__button_sent_confirmation_code)
        return self

    def click_edit_page(self):
        """
        Click on button contacts page
        :return: self
        """
        self._click(self.__click_edit_profile)
        return self

    def click_subscription_ok(self):
        """
        Click on button contacts page
        :return: self
        """
        self._click(self.__button_subscription_ok)
        return self

    def set_name(self, name):
        self._send_keys(self.__name_input, name)
        return self

    def is_note_text_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__subscription_positive)

    def is_set_name_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__name_input)

    def is_set_last_name_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__last_name_input)

    def is_set_surname_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__surname_input)

    def is_set_email_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__email_input)

    def is_set_login_input_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__login_input)

    def is_new_pass_input_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__new_pass_input)

    def is_old_pass_input_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__old_pass_input)

    def is_subscription_positive_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__subscription_positive)

    def is_subscription_error_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__subscription_error)

    def set_last_name(self, last_name):
        """
        Set name in field last_name
        :param last_name: last_name
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

    def set_subscription_email(self, email):
        """
        Set name in field email
        :param email: email
        :return: self
        """
        self._send_keys(self.__subscription_email_input, email)
        return self

    def set_new_pass(self, new_pass):
        """
        Set pass to the field new pass
        :param new_pass: pass
        :return: self
        """
        self._send_keys(self.__new_pass_input, new_pass)
        return self

    def set_old_pass(self, old_pass):
        """
         Set pass to the field old_pass
         :param old_pass: old_pass
         :return: self
         """
        self._send_keys(self.__old_pass_input, old_pass)
        return self
