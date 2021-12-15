

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math




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


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")