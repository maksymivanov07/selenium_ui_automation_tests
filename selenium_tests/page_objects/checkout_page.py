from selenium.webdriver.common.by import By

from selenium_tests.utilities.decorators import auto_step
from selenium_tests.utilities.web_ui.base_page import BasePage


@auto_step
class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __click_make_order = (By.XPATH, "//div[@class='modal-content']//a[@href]")
    __checkout_button = (By.XPATH, "//button[@type='submit']")
    __continue_buying_button = (By.XPATH, "//*[@id='addItemInCart']/div/div/a[2]")
    __click_size_menu = (By.XPATH, "//select")
    __select_size = (By.XPATH, "//select/option[2]")
    __add_to_cart = (By.XPATH, "//a[@rel='nofollow']")
    __message_empty_cart = (By.XPATH, "//div[@class='cart-notetext']")
    __button_add_to_cart = (By.XPATH, "//div[@id='element_buy_button']")
    __button_add_to_fav = (By.XPATH, "//span[@class='favorSpan']")
    __fav_counter = (By.XPATH, "//span[@class='col'][text()='1']")

    def click_add_item_to_fav(self):
        """
        Wait for element and click when it would visible
        :return: self
        """
        self._click(self.__button_add_to_fav)
        return self

    def click_add_to_cart_button(self):
        """
        Wait for element and click when it would visible
        :return: self
        """
        self._click(self.__add_to_cart)
        return self

    def click_size_menu(self):
        """
        Wait for element and click when it would visible
        :return: self
        """
        self._click(self.__click_size_menu)
        return self

    def click_choose_size(self):
        """
        Wait for element and click when it would visible
        :return: self
        """
        self._click(self.__select_size)
        return self

    def click_button_make_order(self):
        """
        Wait for element and click when it would visible
        :return: self
        """
        self._click(self.__click_make_order)
        return self

    def is_checkout_button_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__checkout_button)

    def is_message_empty_cart_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__message_empty_cart)

    def is_continue_buying_button(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__continue_buying_button)

    def is_button_add_to_cart_visible(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__button_add_to_cart)

    def is_item_add_to_fav(self):
        """
        Wait for element would be visible
        :return: True or False
        """
        return self._is_visible(self.__fav_counter)
