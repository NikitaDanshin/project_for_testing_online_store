from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button[value='Add to basket']")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    NAME_BOOK = (By.XPATH, "//h1")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    NAME_BOOK_IN_BASKET = (By.CSS_SELECTOR, ".alertinner strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a")
    BASKET_MESSAGE = (By.ID, "content_inner")