
from .base_page import BasePage
from .locators import ProductPageLocators
import re

class ProductPage(BasePage):


    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        self.solve_quiz_and_get_code()

        # collect messages about adding item into cart and offer available
        message = self.browser.find_elements(*ProductPageLocators.MESSAGE)
        assert "The shellcoder's handbook" in message[0].text, "No message about added item"
        assert "Deferred benefit offer" in message[1].text, "No message about holiday's offer"

        # parsing text of the price of item and total in basket
        price_text = self.browser.find_element(*ProductPageLocators.PRICE).text
        basket_text = self.browser.find_element(*ProductPageLocators.CART).text
        pattern = "total:\ (.*?)\nView"
        basket_price = re.search(pattern, basket_text).group(1)
        assert price_text == basket_price, "Price in basket does'nt match"


