from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.__wait = WebDriverWait(self._driver, 10)

    def __wait_until_element_located(self, locator):
        return self.__wait.until(EC.presence_of_element_located(locator))

    def __wait_until_element_clickable(self, locator):
        return self.__wait.until(EC.element_to_be_clickable(locator))

    def __wait_until_element_clickable_2(self, locator):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def __wait_until_element_visible(self, locator):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def _send_keys(self, locator, value):
        element = self.__wait_until_element_located(locator)
        element.clear()
        element.send_keys(value)

    def _click(self, locator):
        element = self.__wait_until_element_clickable(locator)
        element.click()

    def _clickable(self, locator):
        try:
            self.__wait_until_element_visible(locator)
            self.__wait_until_element_clickable(locator)
            return True
        except TimeoutException:
            return False

    def _is_visible(self, locator):
        try:
            self.__wait_until_element_visible(locator)
            return True
        except TimeoutException:
            return False
