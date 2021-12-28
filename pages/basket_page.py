from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        self.should_be_message_about_not_items_from_basket()

    def should_be_message_about_not_items_from_basket(self):
        assert self.is_element_present(*BasePageLocators.BASKET_MESSAGE), \
            "should be success message"

    def should_be_message_about_not_items_from_basket(self):
        assert self.is_element_present(*BasePageLocators.BASKET_MESSAGE), \
            "should be success message"

