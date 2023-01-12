import pytest


@pytest.mark.regression
def test_add_item_to_cart(open_item_modal_window):
    """
        step 1: click on item
        step 2: choose size
        step 3: click add to card

        actual result: item added to cart
        """
    checkout_page = open_item_modal_window

    if checkout_page.is_continue_buying_button():
        checkout_page \
            .click_button_make_order()
    else:
        checkout_page \
            .click_size_menu() \
            .click_choose_size()\
            .click_add_to_cart_button()\
            .click_go_to_checkout()
    assert checkout_page.is_checkout_button_visible() is True, 'Button checkout is not visible'


@pytest.mark.smoke
def test_cart_is_empty(open_cart_modal_window):
    """
        step 1: click on cart button
        step 2: check cart


        actual result: cart is empty
        """
    checkout_page = open_cart_modal_window
    assert checkout_page.is_message_empty_cart_visible() is True, 'Message is Visible'


@pytest.mark.smoke
def test_transition_to_item_page(open_item_page):
    """
        step 1: click on item
        step 2: check button to interactive


        actual result: button add to cart is visible
        """
    checkout_page = open_item_page
    assert checkout_page.is_button_add_to_cart_visible() is True, 'Button is Visible'


@pytest.mark.smoke
def test_add_to_favorite(open_item_page):
    """
        step 1: click on item
        step 2: click on add item to fav

        actual result: fav counter =1
        """
    checkout_page = open_item_page
    checkout_page.click_add_item_to_fav()
    assert checkout_page.is_item_add_to_fav() is True, 'Button is Visible'
