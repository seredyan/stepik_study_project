
from .base_page import BasePage
from .locators import ProductPageLocators
import re
import time

class ProductPage(BasePage):


    def add_product_to_basket(self):
        self.add_to_basket()
        # self.solve_quiz_and_get_code()

        # collect messages about adding item into cart and offer available
        message = self.browser.find_elements(*ProductPageLocators.MESSAGE)
        product_name = self.get_item_name()

        assert f"{product_name} has been added to your basket" in message[0].text, "No/not_correct message about added item"
        assert "Deferred benefit offer" in message[1].text, "No message about holiday's offer"

        # parsing text of the price of item and total in basket
        price_text = self.get_product_price()
        basket_price = self.get_basket_total()
        assert price_text == basket_price, "Price in basket does'nt match"






        ### auxiliary methods  ####

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE).text

    def get_item_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def get_basket_total(self):
        basket_text = self.browser.find_element(*ProductPageLocators.CART).text
        pattern = "total:\ (.*?)\\nView"
        basket_price = re.search(pattern, basket_text).group(1)
        return basket_price


