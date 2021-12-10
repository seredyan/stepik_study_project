

from selenium.common.exceptions import NoSuchElementException




class BasePage():              ## (similar like by barancev's Applicaton)
    def __init__(self, browser, url):
        self.browser = browser   ## browser inited in conftest.py
        self.url = url



    def open(self):
        self.browser.get(self.url)




    def __init__(self, browser, url, timeout=3):   ## 4_2 step 6
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)



    def is_element_present(self, how, what):    ## 4_2 step 6
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True