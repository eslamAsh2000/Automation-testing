from selenium.webdriver.common.by import By

from PageObjects.loginpage import loginpage


class Mainpage:
    def __init__(self, driver):
        self.driver = driver

    loginbutton = (By.LINK_TEXT, "Log In")

    def loginbuttonfunc(self):
        self.driver.find_element(*Mainpage.loginbutton).click()
        Loginpage = loginpage(self.driver)
        return Loginpage
