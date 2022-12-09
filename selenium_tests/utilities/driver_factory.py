from selenium import webdriver
from selenium.webdriver import Safari

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.safari.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:
    CHROME = 1
    FIREFOX = 2
    SAFARI = 3

    @staticmethod
    def create_driver(driver_id):
        if int(driver_id) == DriverFactory.CHROME:
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif int(driver_id) == DriverFactory.FIREFOX:
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif int(driver_id) == DriverFactory.SAFARI:
            driver = Safari(service=Service())
        else:
            driver = Safari
        return driver
