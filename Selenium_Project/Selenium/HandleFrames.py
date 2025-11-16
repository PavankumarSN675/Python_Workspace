import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.londonfreelance.org/courses/frames/index.html")

frame = driver.find_element(By.NAME, "main")
driver.switch_to.frame(frame)

header_text = driver.find_element(By.CSS_SELECTOR, "body h2").text
print(header_text)

time.sleep(5)
driver.switch_to.default_content()
driver.switch_to.parent_frame()
driver.quit()