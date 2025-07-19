import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://www.python.org/")
driver.maximize_window()
print(f"The url is: {driver.title}")
driver.implicitly_wait(5)
search_bar = driver.find_element(By.XPATH, "//input[@type='search']")
search_bar.clear()
search_bar.send_keys("Getting started with Python")
search_bar.send_keys(Keys.RETURN)
driver.implicitly_wait(5)
time.sleep(10)
driver.quit()
