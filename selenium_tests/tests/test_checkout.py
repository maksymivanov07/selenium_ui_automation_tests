import pytest


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
