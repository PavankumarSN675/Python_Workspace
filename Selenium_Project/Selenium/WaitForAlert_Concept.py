import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://web.whatsapp.com")
time.sleep(5)

wait = WebDriverWait(driver, 10)
alert = wait.until(EC.alert_is_present())
alert.accept()

time.sleep(5)
driver.quit()