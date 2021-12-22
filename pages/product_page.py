from .base_page import BasePage
from .locators import ProductPageLocators
import math
import time

class ProductPage(BasePage):
    def should_be_add_item_to_basket(self):
        self.add_item_to_basket()
        self.solve_quiz_and_get_code()
        time.sleep(5)

    def add_item_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_button.click()

    def should_be_price_in_basket(self):
        price_element = self.browser.find_element(*ProductPageLocators.PRICE)
        #price = price_element.text
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        assert price_element == price_in_basket, "prices not equal"




