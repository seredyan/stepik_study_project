import time

from pages.basket_page import BasketPage
from pages.product_page import ProductPage
import pytest
from pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209"

def test_guest_can_add_product_to_basket(browser):
    browser.delete_all_cookies()
    page = ProductPage(browser, link + "/?promo=newYear2019")  # init Page Object, set to constructor driver and url
    page.open()
    page.add_product_to_basket()



product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{num}" for num in range(10)]
urls[7] = pytest.param(urls[7], marks=pytest.mark.xfail)

@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket_with_promo(browser, link):
    browser.delete_all_cookies()   ### cleans up (for example: basket before adding next item) or before next action
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()



def test_guest_should_see_login_link_on_product_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    browser.delete_all_cookies()
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_checkout_button()
    basket_page.should_be_empty_basket_message_present()


