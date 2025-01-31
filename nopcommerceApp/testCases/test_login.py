import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage


class Test_001_Login:
    baseUrl = "https://opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"

    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        self.driver.close()

        if act_title == "OrangeHRM":
            assert True
        else:
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        time.sleep(5)
        self.lp = LoginPage(self.driver)
        self.lp.setPassword(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(20)
        self.driver.implicitly_wait(400)
        self.driver.save_screenshot(".\\Screenshots\\myfile1.png")

        #self.driver.timeouts(9)
        # act_title1 = self.driver.title
        # print(act_title1)
        # self.driver.save_screenshot(".\\Screenshots\\myfile.png")
        # #self.driver.close()
        # if act_title1 == "Dashboard / nopCommerce administration":
        #     assert True
        # else:
        #     assert False
        acLink = self.driver.current_url
        print(acLink)