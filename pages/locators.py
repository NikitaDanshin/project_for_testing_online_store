from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button[value='Add to basket']")
    PRICE = (By.CLASS_NAME, ".price_color")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".price_color")


