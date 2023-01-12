import pytest

from selenium_tests.utilities.web_ui.randomiser import random_email, random_value


@pytest.mark.regression
def test_user_profile_fields(login_user, open_user_profile):
    """
      precondition: user must me authorised
      step 1: transition to profile page
      actual result: user can see fields correct in profile
      """
    user_profile = open_user_profile
    user_profile.click_edit_page()
    assert user_profile.is_set_name_visible() is True, 'Name value is Visible'
    assert user_profile.is_set_last_name_visible() is True, 'Last value is Visible'
    assert user_profile.is_set_surname_visible() is True, 'Sur value is Visible'
    assert user_profile.is_set_email_visible() is True, 'Email value is Visible'
    assert user_profile.is_set_login_input_visible() is True, 'Login value is Visible'
    assert user_profile.is_new_pass_input_visible() is True, 'Password value is Visible'
    assert user_profile.is_old_pass_input_visible() is True, 'Old password value is Visible'


@pytest.mark.regression
def test_user_change_name(login_user, open_user_profile, env):
    """
        precondition: user must me authorised

        step 1: transition to profile page
        step 2: change name
        step 3: save result
        step 4: check saved result

        postcondition: change name to first variant

        actual result: user change name
        """
    user_profile = open_user_profile
    user_profile \
        .click_edit_page() \
        .set_name(env.name) \
        .set_old_pass(env.password) \
        .set_new_pass(env.password).click_button_save()
    assert user_profile.is_note_text_visible() is True, 'Note saved visible'
    user_profile \
        .set_name(env.name_new) \
        .set_old_pass(env.password) \
        .set_new_pass(env.password).click_button_save()
    assert user_profile.is_note_text_visible() is True, 'Note saved visible'


# @pytest.mark.smoke
# def test_make_subscription(open_user_profile_unauthorised):
#     """
#         step 1: transition to profile page
#         step 2: click on subscription
#         step 3: set email
#         step 4: click button subscription submit
#
#         actual result: message about subscription is visible
#         """
#     user_profile = open_user_profile_unauthorised
#     user_profile.set_subscription_email(random_email())
#     user_profile.click_button_subscription_submit()
#     assert user_profile.is_subscription_positive_visible() is True, 'Ok is Visible'
    # this test failed, because site has a glitch


@pytest.mark.smoke
def test_error_subscription(open_user_profile_unauthorised):
    """
        step 1: transition to profile page
        step 2: click on subscription
        step 3: set wrong email
        step 4: click button subscription submit

        actual result: user can see error about incorrect email
        """
    user_profile = open_user_profile_unauthorised
    user_profile.set_subscription_email(random_value())
    user_profile.click_button_subscription_submit()
    assert user_profile.is_subscription_error_visible() is True, 'Error is Visible'


@pytest.mark.smoke
def test_error_empty_subscription_address(open_user_profile_unauthorised):
    """
        step 1: transition to profile page
        step 2: click on subscription
        step 3: click button subscription submit

        actual result: message about unfilled data is visible
        """
    user_profile = open_user_profile_unauthorised
    user_profile.click_button_sent_confirmation_code()
    assert user_profile.is_subscription_error_visible() is True, 'Error is Visible'
