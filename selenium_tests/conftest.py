import json
import os
from contextlib import suppress

import pytest
import allure

from selenium_tests.page_objects.home_page import HomePage
from selenium_tests.utilities.configuration import Configuration
from selenium_tests.utilities.driver_factory import DriverFactory
from selenium_tests.utilities.web_ui.waits import wait_until
# from selenium_tests.utilities.read_configs import ReadConfig


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def env():
    dir_contain_file = '/Users/max/PycharmProjects/selenium_ui_automation_tests/selenium_tests/configurations'
    os.chdir(dir_contain_file)
    file_name = 'configuration.json'

    with open(file_name) as f:
        data = f.read()
        json_to_dict = json.loads(data)
    return Configuration(**json_to_dict)


@pytest.fixture()
def create_driver(request, env):
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


# create driver with parameters from ini-file
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
def open_about_page(open_home_page):
    return open_home_page.click_contacts_page()


@pytest.fixture()
def open_login_modal_window(open_home_page):
    return open_home_page.click_show_login_form()


@pytest.fixture()
def open_item_page(open_home_page):
    return open_home_page.click_item()


@pytest.fixture()
def open_cart_modal_window(open_home_page):
    return open_home_page.click_cart_button()


@pytest.fixture()
def open_item_modal_window(open_home_page):
    return open_home_page.click_cart_on_item()


@pytest.fixture()
def login_user(open_login_modal_window, env):
    login_user = open_login_modal_window
    wait_until(lambda: login_user.is_login_button_visible(), 'Visible')
    login_user\
        .set_auth_email(env.email)\
        .set_auth_email(env.email)\
        .set_auth_password(env.password)\
        .click_login()
    return login_user


@pytest.fixture()
def open_user_profile(open_home_page):
    return open_home_page.click_show_user_profile()


@pytest.fixture()
def open_user_profile_unauthorised(open_home_page):
    return open_home_page.click_favorite_button().click_subscription_ok()
