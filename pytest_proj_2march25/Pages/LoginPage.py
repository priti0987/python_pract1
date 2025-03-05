from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class LoginPage(BasePage):
    EMAIL = (By.ID,"username")
    PASSWORD = (By.ID,"password")
    LOGIN_Button = (By.ID,"loginBtn")
    SIGNUP_LINK = (By.LINK_TEXT,"Sign up")

    def __init__(self,driver):
        super().__init__(driver)

    def get_login_page_title(self,title):
        return self.get_title(title)

    def signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    def do_loing(self):
        pass

