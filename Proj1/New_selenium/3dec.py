import time

from selenium import webdriver
from selenium.webdriver.common.by import By
#selenium4 ... updated on 13dec2024
driver = webdriver.Chrome()
url = "https://opensource-demo.orangehrmlive.com/"
driver.get(url)
time.sleep(7)
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

act_title = driver.title
exp_title = 'OrangeHRM'
if act_title == exp_title:
    print("Login Test Pass")
else:
    print("Login Test Failed")
time.sleep(10)
print("done....")

