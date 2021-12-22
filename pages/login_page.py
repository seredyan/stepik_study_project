from .base_page import BasePage
from .locators import LoginPageLocators



# url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

class LoginPage(BasePage):

    def should_be_login_page(self):  ## if we have too much pages to test we can get united some of them
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        # assert url is correct

        assert self.browser.current_url.endswith("/login/"), "login is absent in current url"


    def should_be_login_form(self):
        # assert login form is presented
        self.should_be_login_url()
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login email form is not present"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password form is not present"
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), "Login submit button is not present"


    def should_be_register_form(self):
        # assert register form is presented
        self.should_be_login_url()
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Register email form is not present"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), "Register password form is not present"
        assert self.is_element_present(*LoginPageLocators.REGISTER__CONFIRM_PASSWORD), "Register confirm password form is not present"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT), "Register submit button is not present"
