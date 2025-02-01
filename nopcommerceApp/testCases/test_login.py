import time
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen


class Test_001_Login:
    baseUrl = "https://opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"
    logger_ = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger_.info("**************************** Test_001_Login ***********************")
        self.logger_.info("**************************** Verifying Home Page Title  ***********************")
        self.driver = setup
        print(self.baseUrl)
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        self.driver.close()
        self.logger_.info("**************************** Home page Title test is pass ***********************")

        if act_title == "OrangeHRM":
            assert True
        else:
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        time.sleep(5)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
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
