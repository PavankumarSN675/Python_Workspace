import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = None
def setup_module(module):
    global driver
    driver = webdriver.Chrome()
    driver.get('http://www.google.com')
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(10)

def teardown_module(module):
    driver.quit()

def test_google_title():
    assert driver.title == 'Google'

def test_google_url():
    assert driver.current_url == 'https://www.google.com/'