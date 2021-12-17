import pytest
from selenium import webdriver
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.chrome.options import Options as COptions
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--language", "-L", action="store", default="en", help="choose language:en, ru, ...(etc)")
    parser.addoption("--url", "-U", action="store", default="http://selenium1py.pythonanywhere.com/en-gb/", help="choose your browser")


@pytest.fixture(scope="session")
def browser(request):
    browser_param = request.config.getoption("--browser")
    user_language = request.config.getoption("--language")   #  try test_fixture3.py for example to use  #stepik_3.6 step#8
    if browser_param == "chrome":
        # c_options = COptions()
        # c_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # driver = webdriver.Chrome('/Users/sergeysereda/dev/webdrivers/chromedriver', options=c_options)

        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        driver = webdriver.Chrome('/Users/sergeysereda/dev/webdrivers/chromedriver', options=options)

    elif browser_param == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        driver = webdriver.Firefox(firefox_profile=fp)
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.implicitly_wait(10)
    request.addfinalizer(driver.close)
    # driver.get(request.config.getoption("--url"))

    return driver



### option fixture without a language selection option
#
# @pytest.fixture
# def browser(request):
#     browser_param = request.config.getoption("--browser")
#     if browser_param == "chrome":
#         driver = webdriver.Chrome('/Users/sergeysereda/dev/webdrivers/chromedriver')
#     elif browser_param == "firefox":
#         driver = webdriver.Firefox()
#     elif browser_param == "edge":
#         driver = webdriver.Edge(EdgeChromiumDriverManager().install())
#     elif browser_param == "opera":
#         driver = webdriver.Opera(executable_path=OperaDriverManager().install())
#     else:
#         raise Exception(f"{request.param} is not supported!")
#
#     driver.implicitly_wait(10)
#     request.addfinalizer(driver.close)
#     driver.get(request.config.getoption("--url"))
#
#     return driver

