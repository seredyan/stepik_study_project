import time
import random
import string
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
import pytest
from pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209"
links = "http://selenium1py.pythonanywhere.com"

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



class TestUserAddToBasketFromProductPage():

    def test_user_cant_see_success_message(self, browser):  ## 4_3 step 13
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        browser.delete_all_cookies()
        page = ProductPage(browser, link + "/?promo=newYear2019")  # init Page Object, set to constructor driver and url
        page.open()
        page.add_product_to_basket()


    def test_guest_can_get_registered(self, browser):
        page = LoginPage(browser, link)
        page.open()
        email = random_char_email()
        password = random_string()
        page.register_new_user(email, password)
        time.sleep(5)
        page.should_be_authorized_user()









def random_string():
    symbols = string.ascii_letters + string.digits
    return ("".join([random.choice(symbols) for i in range(random.randrange(11, 15))]))

def random_char_email():
    random_emails = ["a@gmail.com", "b@ya.ru", "c@mail.ru", "d@icloud.com", "e@company.com", "f@yahoo.com", "g@outlook.com"]
    symbols = (''.join(random.choice(string.ascii_letters + string.digits) for i in range(random.randrange(5))))
    return (symbols + random.choice(random_emails))