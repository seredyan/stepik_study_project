import time

from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage):

   def __init__(self, *args, **kwargs):    ## 4_3 step 8
      super(MainPage, self).__init__(*args, **kwargs)  ## 4_3 step 8
