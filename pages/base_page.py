

from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class BasePage():              ## (similar like by barancev's Applicaton)
    def __init__(self, browser, url):
        self.browser = browser   ## browser inited in conftest.py
        self.url = url



    def open(self):
        self.browser.get(self.url)




    def __init__(self, browser, url, timeout=1):   ## 4_2 step 6
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)



    def is_element_present(self, how, what):    ## 4_2 step 6
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True



    def is_not_element_present(self, how, what, timeout=3):  ## 4_3 step 5
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False



    def is_disappeared(self, how, what, timeout=10):     ## 4_3 step 5
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True





    def solve_quiz_and_get_code(self):     ## code for quiz on learning's web sites
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