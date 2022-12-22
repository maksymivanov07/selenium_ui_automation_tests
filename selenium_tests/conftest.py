import json
from contextlib import suppress

import pytest
import allure

from selenium_tests.page_objects.about_page import AboutPage
from selenium_tests.page_objects.home_page import HomePage
from selenium_tests.page_objects.login_page import LoginPage
from selenium_tests.page_objects.checkout_page import CheckoutPage
from selenium_tests.page_objects.user_profile_page import UserProfilePage
from selenium_tests.utilities.configuration import Configuration
from selenium_tests.utilities.driver_factory import DriverFactory
from selenium_tests.utilities.read_configs import ReadConfig


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def env():
    with open(
            '/Users/max/PycharmProjects/selenium_ui_automation_tests/selenium_tests/configurations/configuration.json') as file:
        env_dict = json.loads(file.read())
    return Configuration(**env_dict)


@pytest.fixture()
def create_driver(env, request):
    driver = DriverFactory.create_driver(driver_id=env.browser_id)
    driver.set_window_size(1920, 1080)
    driver.get(env.base_url)
    yield driver
    if request.node.rep_call.failed:
        with suppress(Exception):
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
    driver.quit()


# @pytest.fixture()
# def create_driver(request):
#     driver = DriverFactory.create_driver(ReadConfig.get_browser_data())
#     driver.get(ReadConfig.get_base_url())
#     driver.set_window_size(1920, 1080)
#     yield driver
#     if request.node.rep_call.failed:
#         with suppress(Exception):
#             allure.attach(driver.get_screenshot_as_png(), name=request.function.__name__,
#                           attachment_type=allure.attachment_type.PNG)
#     driver.quit()


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
