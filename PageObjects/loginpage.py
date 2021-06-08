from selenium.webdriver.common.by import By


class loginpage:
    def __init__(self, driver):
        self.driver = driver

    email = (By.XPATH, "//input[@id='login-email']")
    password = (By.CSS_SELECTOR, "#login-password")
    nextbutton = (By.XPATH, "//span[contains(text(),' Next ')]")
    rememberbutton = (By.XPATH, "//span[contains(text(),'Remember email address')]")
    signinbutton = (By.XPATH, "//span[contains(text(),'Sign in')]")
    Explorebutton = (By.XPATH,"//a[@aria-label='Explore']")
    picavatar = (By.XPATH, "//div[@style='background-image: url(//combo.staticflickr.com/pw/images/buddyicon10.png#192793682@N07)']")
    logout =  (By.LINK_TEXT, "Log out")
    clearall = (By.XPATH,"//div[contains(text(),'Clear all')]")

    def getemail(self):
        return self.driver.find_element(*loginpage.email)

    def getpassword(self):
        return self.driver.find_element(*loginpage.password)

    def getnext(self):
        return self.driver.find_element(*loginpage.nextbutton)

    def getrememberbutton(self):
        return self.driver.find_element(*loginpage.rememberbutton)

    def getsigninbutton(self):
        return self.driver.find_element(*loginpage.signinbutton)

    def getpicavatar(self):
        return self.driver.find_element(*loginpage.picavatar)

    def getlogout(self):
        return self.driver.find_element(*loginpage.logout)

    def getclearall(self):
        return self.driver.find_element(*loginpage.clearall)

    def getexplorebutton(self):
        return self.driver.find_element(*loginpage.Explorebutton)