import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
url = "https://opensource-demo.orangehrmlive.com/"
#driver.get("https://blazedemo.com/")
driver.get(url)
time.sleep(7)

driver.maximize_window()

driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")


time.sleep(10)
print("done....")