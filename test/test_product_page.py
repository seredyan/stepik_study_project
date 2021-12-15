
from pages.product_page import ProductPage

offer_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"

# link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, offer_link)  # init Page Object, set to constructor driver and url
    page.open()

    page.add_product_to_basket()

