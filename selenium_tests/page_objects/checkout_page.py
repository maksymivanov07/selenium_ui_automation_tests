from selenium.webdriver.common.by import By

from selenium_tests.utilities.web_ui.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __click_item = (By.XPATH, "//div[@class='new-items-content catalog-lvl2']/div[1]")
    __click_cart_on_item = (By.XPATH, "//div[@class='new-items-content catalog-lvl2']/div[1]//div[@class='bottom']")
    __continue_buying_button = (By.XPATH, "//*[@id='addItemInCart']/div/div/a[2]")
    __cart_button = (By.XPATH, "//*[@id='shopping-cart_4_']")
    __click_size_menu = (By.XPATH, "//select")
    __select_size = (By.XPATH, "//select/option[2]")
    __add_to_cart = (By.XPATH, "//a[@rel='nofollow']")
    __message_empty_cart = (By.XPATH, "//div[@class='cart-notetext']")
    __proceed_to_checkout = (By.XPATH, "//*[@id='addItemInCart']/div/div/a[1]")
    __button_add_to_cart = (By.XPATH, "//div[@id='element_buy_button']")
    __button_add_to_fav = (By.XPATH, "//span[@class='favorSpan']")
    __fav_counter = (By.XPATH, "//span[@class='col'][text()='1']")

    def click_item(self):
        self._click(self.__click_item)
        return self

    def click_cart_on_item(self):
        self._click(self.__click_cart_on_item)
        return self

    def click_add_item_to_fav(self):
        self._click(self.__button_add_to_fav)
        return self

    def click_continue_buying_button(self):
        self._click(self.__continue_buying_button)
        return self

    def click_add_to_cart_button(self):
        self._click(self.__add_to_cart)
        return self

    def click_size_menu(self):
        self._click(self.__click_size_menu)
        return self

    def click_cart_button(self):
        self._click(self.__cart_button)
        return self

    def click_proceed_to_checkout_button(self):
        self._click(self.__proceed_to_checkout)
        return self

    def click_choose_size(self):
        self._click(self.__select_size)
        return self

    def is_message_empty_cart_visible(self):
        return self._is_visible(self.__message_empty_cart)

    def is_button_add_to_cart_visible(self):
        return self._is_visible(self.__button_add_to_cart)

    def is_item_add_to_fav(self):
        return self._is_visible(self.__fav_counter)
