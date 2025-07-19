import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("https://cosmocode.io/automation-practice-webtable/")
# driver.maximize_window()
# rows = len(driver.find_elements(By.XPATH, value="//table[@id='countries']/tbody/tr"))
# cols = len(driver.find_elements(By.XPATH, value="//table[@id='countries']/tbody/tr[2]/td"))
# print(rows)
# print(cols)
# found_value = None
# link = None
# for row in range(2, rows + 1):
#     for col in range(2, cols + 1):
#         xpath = f"//table[@id='countries']/tbody/tr[{row}]/td[{col}]"
#         value = driver.find_element(By.XPATH, value=xpath)
#         if value == "Euro":
#             link = value.find_elements(By.TAG_NAME, value="a")
#             found_value = value
#
# print(f"{found_value=}")
# print(f"{link=}")

driver = webdriver.Chrome()
driver.get("https://leetcode.com/contest/weekly-contest-309/ranking/?region=global_v2")
driver.maximize_window()
rows = len(driver.find_elements(By.XPATH, value="//*[@class='flex min-w-[fit-content] flex-col']/div"))
cols = len(driver.find_elements(By.XPATH, value="//*[@class='flex min-w-[fit-content] flex-col']/div[1]/div"))
print(rows)
print(cols)
found_value = None
link = None
for row in range(2, rows + 1):
    for col in range(2, cols + 1):
        xpath = f"//*[@class='flex min-w-[fit-content] flex-col']/div[{row}]/div[{col}]"
        value = driver.find_element(By.XPATH, value=xpath).text
        print(f"{value=}")
        # print(f"{link=}")
        # if value == "Euro":
        #     link = value.find_elements(By.TAG_NAME, value="a")
        #     found_value = value

# print(f"{found_value=}")
# print(f"{link=}")

time.sleep(2)
driver.quit()
