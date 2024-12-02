import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Chrome()
driver.get("https://blazedemo.com/")
driver.maximize_window()
title = driver.find_element(By.XPATH,"//input[@value='Find Flights']")
print(title.is_displayed())
title.click()
tbody = driver.find_element(By.XPATH,"//table[@class='table']/tbody")
print(tbody)
# data = []
# for tr in tbody:
#     row = [item.text for item in tr.find_elements(By.XPATH,'//td[6]')]
#     data.append(row.text)
#     print(row)
# data= data[0]
# data1=[]
# for i in data:
#     okitem  = i[1:len(i)+1]
#     # print(okitem)
#     okitemf = float(okitem)
#     data1.append(okitemf)
#
# (data1.sort())
# # print(data1)
# print(data1[0])
# lowprice = str (data1[0])
# # print(lowprice)
# # print(type(lowprice))
#
# # for tr in tbody:
# #     row = [item.text for item in tr.find_elements(By.XPATH,'//td[6]')]
# #     data.append(row)
# #     print(row)
#
#
# #
# # driver.get("https://www.yatra.com")
# # driver.maximize_window()
# # driver.implicitly_wait(4)
# # title = driver.find_element(By.XPATH,"//a[@title='Multicity']")
# # print(title.is_displayed())
# # title.click()
time.sleep(10)
print("Done...!")