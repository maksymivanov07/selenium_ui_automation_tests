import pytest

from selenium_tests.utilities.web_ui.randomiser import random_phone, random_email, random_name, random_value


@pytest.mark.regression
def test_registration(open_home_page, env):
    """
    step 1: user open registration form
    step 2: user fill name
    step 3: user fill last name
    step 4: user fill random email
    step 5: user fill random password
    step 6: user fill same password to confirm
    step 7: user fill phone number
    step 8: user click register

    actual result: user registered
    """
    home_page = open_home_page
    home_page.click_show_registration_form()
    home_page.set_name(random_name()) \
        .set_name(random_name()) \
        .set_last_name(random_name()) \
        .set_email(random_email()) \
        .set_password(env.password) \
        .set_confirm_password(env.password) \
        .set_phone_number(random_phone())
    home_page.click_register()
    assert home_page.is_logout_button_visible() is True, 'Button is not visible'


@pytest.mark.regression
def test_incorrect_phone(open_home_page, env):
    """
    step 1: user open registration form
    step 2: user fill name
    step 3: user fill last name
    step 4: user fill random email
    step 5: user fill random password
    step 6: user fill same password to confirm
    step 7: user fill phone number in incorrect format
    step 8: user click register

    actual result: user can see error about incorrect phone number
    """
    home_page = open_home_page
    home_page.click_show_registration_form()
    home_page.set_name(env.name)\
        .set_name(env.name)  \
        .set_last_name(env.last_name) \
        .set_email(env.email) \
        .set_password(env.password) \
        .set_confirm_password(env.password) \
        .set_phone_number(random_value()) \
        .click_register()
    assert open_home_page.is_error_phone_number_visible() is True, 'Error phone number is Visible'


@pytest.mark.smoke
def test_empty_fields_error(open_home_page):
    """
    step 1: user open registration form
    step 2: user click register

    actual result: user can see errors from each other field about empty field
    """
    home_page = open_home_page
    home_page.click_show_registration_form().click_register()
    assert open_home_page.is_error_name_visible() is True, 'Error name is Visible'
    assert open_home_page.is_error_last_name_visible() is True, 'Error last name is Visible'
    assert open_home_page.is_error_email_visible() is True, 'Error email is Visible'
    assert open_home_page.is_error_password_visible() is True, 'Error password is Visible'
    assert open_home_page.is_error_is_empty_visible() is True, 'Error password confirmation is Visible'


@pytest.mark.smoke
def test_incorrect_password_confirmation_error(open_home_page, env):
    """
    step 1: user open registration form
    step 2: user click register
    step 3: user type two different passwords

    actual result: user can see error about incorrect password confirmation
    """
    home_page = open_home_page
    home_page.click_show_registration_form().click_register()
    home_page.set_password(env.password).set_confirm_password(random_value())
    assert open_home_page.is_error_password_is_not_equal_visible() is False, 'Error password confirmation is Visible'


@pytest.mark.smoke
def test_show_phone_numbers(open_home_page):
    """
     step 1: user open home page
     step 3: user click dropdown with phone

     actual result: user can see additional number in dropdown-menu
     """
    home_page = open_home_page
    home_page.click_phone_dropdown()
    assert open_home_page.is_additional_number_visible() is True, 'Additional number is Visible'
