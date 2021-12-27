import pytest
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    #link =f"{link}"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_item_to_basket()
    page.should_be_names_in_basket()
    page.should_be_prices_in_basket()