
from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

def test_guest_can_see_login_form(browser):
    page = LoginPage(browser, link)  # init Page Object, set to constructor driver and url
    page.open()
    page.should_be_login_form()


def test_guest_can_see_register_form(browser):
    page = LoginPage(browser, link)  # init Page Object, set to constructor driver and url
    page.open()
    page.should_be_register_form()


