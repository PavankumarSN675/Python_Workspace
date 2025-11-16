import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = None

@pytest.fixture(scope="module")
def init_driver():
    global driver
    print("--------------Init driver-------------------")
    driver = webdriver.Chrome()
    driver.get('http://www.google.com')
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(10)

    yield
    print("------------teardown driver------------------")
    driver.quit()

# Approach 1
# def test_google_title(init_driver):
#     assert driver.title == 'Google'
#
# def test_google_url(init_driver):
#     assert driver.current_url == 'https://www.google.com/'

# Approach 2
@pytest.mark.usefixtures("init_driver")
def test_google_title():
    assert driver.title == 'Google'

@pytest.mark.usefixtures("init_driver")
def test_google_url():
    assert driver.current_url == 'https://www.google.com/'