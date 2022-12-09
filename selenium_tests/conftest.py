import pytest

from selenium_tests.page_objects.about_page import AboutPage
from selenium_tests.page_objects.home_page import HomePage
from selenium_tests.page_objects.login_page import LoginPage
from selenium_tests.page_objects.checkout_page import CheckoutPage
from selenium_tests.page_objects.user_profile_page import UserProfilePage
from selenium_tests.utilities.driver_factory import DriverFactory
from selenium_tests.utilities.read_configs import ReadConfig


@pytest.fixture(scope='session')
def create_driver():
    driver = DriverFactory.create_driver(ReadConfig.get_browser_data())
    driver.get(ReadConfig.get_base_url())
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


@pytest.fixture()
def open_home_page(create_driver):
    return HomePage(create_driver)


@pytest.fixture()
def open_about_page(create_driver):
    return AboutPage(create_driver)


@pytest.fixture()
def open_login_page(create_driver):
    return LoginPage(create_driver)


@pytest.fixture()
def open_checkout_page(create_driver):
    return CheckoutPage(create_driver)


@pytest.fixture()
def open_user_profile_page(create_driver):
    return UserProfilePage(create_driver)
