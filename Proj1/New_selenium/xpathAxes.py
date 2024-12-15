from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url= "https://money.rediff.com/gainers/bse/daily/groupa"

driver.get(url)
time.sleep(7)
driver.maximize_window()
#self
# text_msg= driver.find_element(By.XPATH,"//a[contains(text(),'Hatsun')]")
#print(text_msg.is_displayed())
#print(text_msg.text)

#parent
text_msg= driver.find_element(By.XPATH,"//a[contains(text(),'Hatsun')]/parent::td")
print(text_msg.text)
time.sleep(10)
print("done....")

# Child
# Parent
# Following
# Preceding
# Following-sibling
# Preceding-sibling
# Ancestor
# Descendant

