
## stepik 4_2 step 7


from selenium.webdriver.common.by import By


class MainPageLocators():
    pass




class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_SUBMIT = (By.NAME, "login_submit")

    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER__CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT = (By.NAME, "registration_submit")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, " #add_to_basket_form")
    MESSAGES = (By.CSS_SELECTOR, ".alertinner")
    CART = (By.CLASS_NAME, "basket-mini")
    PRICE = (By.CSS_SELECTOR, ".col-sm-6 .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_MESSAGE = (By.CSS_SELECTOR, ".alertinner p strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
