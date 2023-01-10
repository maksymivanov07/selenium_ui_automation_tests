import pytest

from selenium_tests.utilities.web_ui.waits import wait_until
from selenium_tests.utilities.web_ui.randomiser import random_value, random_email
import time


@pytest.mark.regression
def test_loging(open_login_modal_window, login_user, env):
    """
      step 1: user open login form
      step 2: user fill login and password
      step 8: user click register

      actual result: user authorised
      """
    login_page = open_login_modal_window
    wait_until(lambda: login_page.is_login_button_visible(), 'Visible')
    auth_user = login_user
    assert auth_user.is_login_button_visible() is True, 'Login button is visible'


@pytest.mark.smoke
def test_login_form_empty_fields_error(open_login_modal_window):
    """
      step 1: user open login form
      step 2: user click login

      actual result: user can see errors about empty fields
      """
    login_page = open_login_modal_window
    login_page.click_login()
    assert login_page.is_error_email_visible() is True, 'Error email is visible'
    assert login_page.is_error_password_visible() is True, 'Error password is visible'


@pytest.mark.smoke
def test_forgot_password_error(open_login_modal_window):
    """
      step 1: user open login form
      step 2: user click button "forgot password"

      actual result: user transition to restore password page
      """
    login_page = open_login_modal_window
    login_page \
        .click_forgot_password() \
        .set_forgott_password_email(random_email()) \
        .click_send_email()
    assert login_page.is_error_user_not_found_visible() is True, 'Error is not visible'


@pytest.mark.smoke
def test_incorrect_login(open_login_modal_window):
    """
      step 1: user open login form
      step 2: user fill incorrect data on fields
      step 3: user click login

      actual result: user is not authorised and see an error
      """
    login_page = open_login_modal_window
    login_page.set_auth_email(random_value())
    login_page.set_auth_email(random_value())\
        .set_auth_password(random_value())\
        .click_login()
    assert login_page.is_error_login_visible() is True, 'Error login is visible'
