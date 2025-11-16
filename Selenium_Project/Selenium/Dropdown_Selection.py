import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.orangehrm.com/en/30-day-free-trial")
driver.maximize_window()
print(driver.title)

dropdown_box = driver.find_element(By.XPATH, value="//select[@name='Country']")
sel_ele = Select(dropdown_box)
sel_ele.select_by_visible_text('India')

time.sleep(5)
driver.quit()