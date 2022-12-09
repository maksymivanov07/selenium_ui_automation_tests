import pytest

from selenium_tests.utilities.web_ui.waits import wait_until
from selenium_tests.utilities.web_ui.randomiser import random_phone, random_email


@pytest.mark.regression
def test_registration(open_home_page):
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
    home_page.set_name('Max') \
        .set_last_name('Ivanov') \
        .set_email(random_email()) \
        .set_password('Pa$$w0rd_max') \
        .set_confirm_password('Pa$$w0rd_max') \
        .set_phone_number(random_phone()) \
        .click_register()


@pytest.mark.regression
def test_incorrect_phone(open_home_page):
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
    home_page.set_name('Maksym') \
        .set_last_name('Ivanov') \
        .set_email('vedmak2@gmail.com') \
        .set_password('Pa$$w0rd_max') \
        .set_confirm_password('Pa$$w0rd_max') \
        .set_phone_number('9876523') \
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
def test_incorrect_password_confirmation_error(open_home_page):
    """
    step 1: user open registration form
    step 2: user click register
    step 3: user type two different passwords

    actual result: user can see error about incorrect password confirmation
    """
    home_page = open_home_page
    home_page.click_show_registration_form().click_register()
    home_page.set_password('Pa$$w0rd_max').set_confirm_password('asdasdfadsf')
    assert open_home_page.is_error_password_is_not_equal_visible() is True, 'Error password confirmation is Visible'


@pytest.mark.smoke
def test_show_phone_numbers(open_home_page):
    """
     step 1: user open home page
     step 3: user click dropdown with phone

     actual result: user can see additional number in dropdown-menu
     """
    home_page = open_home_page
    home_page.click_phone_dropdown()
    assert open_home_page.is_additional_phone_visible() is True, 'Additional number is Visible'


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


@pytest.mark.regression
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


@pytest.mark.regression
def test_user_profile_fields(open_user_profile_page, open_login_page):
    """
      precondition: user must me authorised

      step 1: transition to profile page

      actual result: user can see fields correct in profile
      """
    user_profile = open_user_profile_page
    login_page = open_login_page
    login_page.click_show_login_form()
    wait_until(lambda: login_page.is_login_button_visible(), 'Visible')
    home_page = login_page.login('vedmak2@gmail.com', 'Pa$$w0rd_max')
    wait_until(lambda: home_page.is_logout_button_visible(), 'Visible')
    login_page.click_show_user_profile()
    user_profile.click_edit_page()
    assert user_profile.is_set_name_visible() is True, 'Name value is Visible'
    assert user_profile.is_set_last_name_visible() is True, 'Last value is Visible'
    assert user_profile.is_set_surname_visible() is True, 'Sur value is Visible'
    assert user_profile.is_set_email_visible() is True, 'Email value is Visible'
    assert user_profile.is_set_login_input_visible() is True, 'Login value is Visible'
    assert user_profile.is_new_pass_input_visible() is True, 'Password value is Visible'
    assert user_profile.is_old_pass_input_visible() is True, 'Old password value is Visible'


@pytest.mark.regression
def test_user_change_name(open_user_profile_page, open_login_page):
    """
        precondition: user must me authorised

        step 1: transition to profile page
        step 2: change name
        step 3: save result
        step 4: check saved result

        postcondition: change name to first variant

        actual result: user change name
        """
    user_profile = open_user_profile_page
    login_page = open_login_page
    login_page.click_show_login_form()
    wait_until(lambda: login_page.is_login_button_visible(), 'Visible')
    home_page = login_page.login('vedmak2@gmail.com', 'Pa$$w0rd_max')
    wait_until(lambda: home_page.is_logout_button_visible(), 'Visible')
    login_page.click_show_user_profile()
    user_profile \
        .click_edit_page() \
        .set_name('Max') \
        .set_old_pass('Pa$$w0rd_max') \
        .set_new_pass('Pa$$w0rd_max').click_button_save()
    assert user_profile.is_note_text_visible() is True, 'Note saved visible'
    user_profile \
        .set_name('Максим') \
        .set_old_pass('Pa$$w0rd_max') \
        .set_new_pass('Pa$$w0rd_max').click_button_save()
    assert user_profile.is_note_text_visible() is True, 'Note saved visible'


@pytest.mark.smoke
def test_make_subscription(open_user_profile_page):
    """
        step 1: transition to profile page
        step 2: click on subscription
        step 3: set email
        step 4: click button subscription submit

        actual result: message about subscription is visible
        """
    user_profile = open_user_profile_page
    user_profile.click_subscription_ok()
    user_profile.set_subscription_email('09876574sldfj@gmail.com')
    user_profile.click__button_subscription_submit()
    assert user_profile.is_subscription_positive_visible() is True, 'Ok is Visible'


@pytest.mark.smoke
def test_error_subscription(open_user_profile_page):
    """
        step 1: transition to profile page
        step 2: click on subscription
        step 3: set wrong email
        step 4: click button subscription submit

        actual result: user can see error about incorrect email
        """
    user_profile = open_user_profile_page
    user_profile.click_subscription_ok()
    user_profile.set_subscription_email('87654')
    user_profile.click__button_subscription_submit()
    assert user_profile.is_subscription_error_visible() is True, 'Error is Visible'


@pytest.mark.smoke
def test_error_empty_subscription_address(open_user_profile_page):
    """
        step 1: transition to profile page
        step 2: click on subscription
        step 3: click button subscription submit

        actual result: message about unfilled data is visible
        """
    user_profile = open_user_profile_page
    user_profile.click_subscription_ok().click_button_sent_confirmation_code()
    assert user_profile.is_subscription_error_visible() is True, 'Error is Visible'


@pytest.mark.regression
def test_add_item_to_cart(open_checkout_page):
    """
        step 1: click on item
        step 2: choose size
        step 3: click add to card

        actual result: item added to cart
        """
    checkout_page = open_checkout_page
    checkout_page.click_cart_on_item() \
        .click_size_menu() \
        .click_choose_size() \
        .click_add_to_cart_button()


@pytest.mark.regression
def test_transition_from_cart_to_checkout(open_checkout_page):
    """
        step 1: click on item
        step 2: choose size
        step 3: click add to card
        step 4: click continue

        actual result: user transition to checkout
        """
    checkout_page = open_checkout_page
    checkout_page.click_cart_on_item() \
        .click_size_menu() \
        .click_choose_size() \
        .click_add_to_cart_button() \
        .click_proceed_to_checkout_button()


@pytest.mark.smoke
def test_cart_is_empty(open_checkout_page):
    """
        step 1: click on cart button
        step 2: check cart


        actual result: cart is empty
        """
    checkout_page = open_checkout_page
    checkout_page \
        .click_cart_button()
    assert checkout_page.is_message_empty_cart_visible() is True, 'Message is Visible'


@pytest.mark.smoke
def test_transition_to_item_page(open_checkout_page):
    """
        step 1: click on item
        step 2: check button to interactive


        actual result: button add to cart is visible
        """
    checkout_page = open_checkout_page
    checkout_page.click_item()
    assert checkout_page.is_button_add_to_cart_visible() is True, 'Button is Visible'


@pytest.mark.smoke
def test_add_to_favorite(open_checkout_page):
    """
        step 1: click on item
        step 2: click on add item to fav

        actual result: fav counter =1
        """
    checkout_page = open_checkout_page
    checkout_page.click_item().click_add_item_to_fav()
    assert checkout_page.is_item_add_to_fav() is True, 'Button is Visible'
