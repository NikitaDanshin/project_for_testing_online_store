from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def should_be_add_item_to_basket(self):
        self.add_item_to_basket()
        self.solve_quiz_and_get_code()
        time.sleep(5)

    def add_item_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_button.click()

    def should_be_names_in_basket(self):
        name_element = self.browser.find_element(*ProductPageLocators.NAME_BOOK)
        name = name_element.text
        name_element_2 = self.browser.find_element(*ProductPageLocators.NAME_BOOK_IN_BASKET)
        name_element_in_basket = name_element_2.text
        assert name == name_element_in_basket, "names are not equals"


    def should_be_prices_in_basket(self):
        price_element = self.browser.find_element(*ProductPageLocators.PRICE)
        price = price_element.text
        price_element_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        price_in_basket = price_element_in_basket.text
        assert price == price_in_basket, "prices are not equals"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_BOOK_IN_BASKET), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.NAME_BOOK_IN_BASKET), \
            "Success message is presented, but should not be"

