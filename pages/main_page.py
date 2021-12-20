
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage):
   def __init__(self, *args, **kwargs):    ## 4_3 step 8
      super(MainPage, self).__init__(*args, **kwargs)  ## 4_3 step 8



      # alert = self.browser.switch_to.alert  # in case if alert be added
      # alert.accept()

      # login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
      # login_link.click()


