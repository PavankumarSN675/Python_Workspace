import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://jqueryui.com/resources/demos/droppable/default.html")

action = ActionChains(driver)
source = driver.find_element(By.ID, value="draggable")
target = driver.find_element(By.ID, value="droppable")

# Option 1
action.drag_and_drop(source, target).perform()
# Option 2
# action.click_and_hold(source).move_to_element(target).release().perform()

time.sleep(5)
driver.quit()