import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://app.hubspot.com/login")
driver.maximize_window()

# Implicit wait
driver.implicitly_wait(10)

# Explicit wait
wait = WebDriverWait(driver, 10)
email = wait.until(EC.presence_of_element_located((By.ID, "username")))
email.send_keys("test@gmail.com")

driver.find_element(By.ID, "password").send_keys("test@123")

time.sleep(5)
driver.quit()

