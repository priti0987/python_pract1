
class LoginPage:
    testbox_username_id = "username"
    testbox_password_id = "password"
    button_login_xpath="//button[@type='submit']"
    link_logout_xpath = "//a[contains(@href,'logout')]"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element("name",self.testbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element("name",self.testbox_password_id).send_keys(password)

    def clickLogin(self):
        print((self.driver.find_element("xpath", self.button_login_xpath)).is_visible)
        self.driver.find_element("xpath", self.button_login_xpath).click
        self.driver.find_element("xpath", self.button_login_xpath).click

    def clickLogout(self):
        self.driver.find_element("xpath",self.link_logout_xpath).click
