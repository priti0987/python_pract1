from selenium.webdriver import Keys


class LoginPage:
    testbox_username_xpath = "//input[@name='username']"
    testbox_password_xpath = "//input[@name='password']"
    button_login_xpath="//button[@type='submit']"
    link_logout_xpath = "//a[contains(@href,'logout')]"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element("xpath",self.testbox_username_xpath).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element("xpath",self.testbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element("xpath", self.button_login_xpath).send_keys(Keys.RETURN)
        # self.driver.find_element("xpath", self.button_login_xpath).click

    def clickLogout(self):
        self.driver.find_element("xpath",self.link_logout_xpath).click
