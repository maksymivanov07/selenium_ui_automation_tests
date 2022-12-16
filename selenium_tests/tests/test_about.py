import allure
import pytest

from selenium_tests.utilities.web_ui.waits import wait_until
from selenium_tests.utilities.web_ui.randomiser import random_phone, random_email


@pytest.mark.smoke
def test_callback_sent(open_about_page):
    """
      step 1: user transition to about page
      step 2: user fill login, email, message
      step 3: user click submit

      actual result: user submit message
      """
    about_page = open_about_page
    about_page.click_contacts_page()
    about_page.set_name('TestUsername').set_email('randommail@gmail.com').set_message(
        'Help me please').click_submit_button()


@pytest.mark.regression
def test_incorrect_email_error(open_about_page):
    """
      step 1: user transition to about page
      step 2: user fill name
      step 3: user fill email in incorrect format
      step 4: user click submit

      actual result: user see error about incorrect email
      """
    about_page = open_about_page
    about_page.click_contacts_page()
    about_page.set_name('TestUsername').set_email('3456789').click_submit_button()
    about_page.click_submit_button()
    assert about_page.is_error_wrong_email_visible() is True, 'Error email is Visible'


@pytest.mark.smoke
def test_callback_empty_fields_error(open_about_page):
    """
      step 1: user transition to about page
      step 2: user click submit

      actual result: user see error about unfilled fields
      """
    about_page = open_about_page
    about_page.click_contacts_page()
    about_page.click_submit_button()
    assert about_page.is_error_name_visible() is True, 'Error name is Visible'
    assert about_page.is_error_email_visible() is True, 'Error email is Email'
    assert about_page.is_error_message_visible() is True, 'Error message is Message'
    assert about_page.is_error_captcha_visible() is True, 'Error captcha is Captcha'


@pytest.mark.smoke
def test_phone_number_clickable(open_about_page):
    """
      step 1: user transition to about page
      step 2: user check button to interation

      actual result: phone number is clickable
      """
    about_page = open_about_page
    about_page.click_contacts_page()
    assert about_page.is_phone_number_clickable() is True, 'Is phone number Clickable'
