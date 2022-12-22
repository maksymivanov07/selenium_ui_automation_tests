import pytest

from selenium_tests.utilities.web_ui.waits import wait_until
from selenium_tests.utilities.web_ui.randomiser import random_phone, random_email


@pytest.mark.regression
def test_loging(open_login_page):
    """
      step 1: user open login form
      step 2: user fill login and password
      step 8: user click register

      actual result: user authorised
      """
    login_page = open_login_page
    login_page.click_show_login_form()
    wait_until(lambda: login_page.is_login_button_visible(), 'Visible')
    home_page = login_page.login('vedmak2@gmail.com', 'Pa$$w0rd_max')
    wait_until(lambda: home_page.is_logout_button_visible(), 'Visible')


@pytest.mark.smoke
def test_login_form_empty_fields_error(open_login_page):
    """
      step 1: user open login form
      step 2: user click login

      actual result: user can see errors about empty fields
      """
    login_page = open_login_page
    login_page.click_show_login_form()
    login_page.click_login()
    assert login_page.is_error_email_visible() is True, 'Error email is visible'
    assert login_page.is_error_password_visible() is True, 'Error password is visible'


@pytest.mark.smoke
def test_forgot_password(open_login_page):
    """
      step 1: user open login form
      step 2: user click button "forgot password"

      actual result: user transition to restore password page
      """
    login_page = open_login_page
    login_page.click_show_login_form()
    login_page.click_forgot_password()
    assert login_page.is_send_button_visible() is True, 'Button page is visible'


@pytest.mark.smoke
def test_incorrect_login(open_login_page):
    """
      step 1: user open login form
      step 2: user fill incorrect data on fields
      step 3: user click login

      actual result: user is not authorised and see an error
      """
    login_page = open_login_page
    login_page.click_show_login_form()
    login_page.set_auth_email('23456789').set_auth_password('234567898').click_login()
    assert login_page.is_error_login_visible() is True, 'Error login is visible'