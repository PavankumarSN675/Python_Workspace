import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://amazon.com")
driver.maximize_window()

driver.get_screenshot_as_file(filename="amazon.png")

time.sleep(5)
driver.quit()
