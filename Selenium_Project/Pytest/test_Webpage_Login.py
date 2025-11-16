import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

def test_google():
    driver = webdriver.Chrome()
    driver.get('http://www.google.com')
    driver.maximize_window()
    driver.implicitly_wait(10)
    assert driver.title == 'Google'
    driver.quit()

def test_facebook():
    driver = webdriver.Chrome()
    driver.get('http://www.facebook.com')
    driver.maximize_window()
    driver.implicitly_wait(10)
    assert driver.title == 'Facebook – log in or sign up'
    driver.quit()

def test_instagram():
    driver = webdriver.Chrome()
    driver.get('http://www.instagram.com')
    driver.maximize_window()
    driver.implicitly_wait(10)
    assert driver.title == 'Instagram'
    driver.quit()

def test_gmail():
    driver = webdriver.Chrome()
    driver.get('http://www.gmail.com')
    driver.maximize_window()
    driver.implicitly_wait(10)
    assert driver.title == 'Gmail'
    driver.quit()

def test_rediff():
    driver = webdriver.Chrome()
    driver.get('http://www.rediff.com')
    driver.maximize_window()
    driver.implicitly_wait(10)
    assert driver.title == 'Advertisement'
    driver.quit()