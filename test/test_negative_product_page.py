

from pages.product_page import ProductPage
import pytest

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209"

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)# + "/?promo=newYear2019")  # init Page Object, set to constructor driver and url
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)# + "/?promo=newYear2019")  # init Page Object, set to constructor driver and url
    page.open()
    page.should_not_be_success_message()



def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)# + "/?promo=newYear2019")  # init Page Object, set to constructor driver and url
    page.open()
    page.add_product_to_basket()
    page.success_message_should_be_disappeart()