import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Tools.Baseclass import baseclass
from PageObjects.Mainpage import Mainpage
from PageObjects.loginpage import loginpage


class Testsignup():
    @pytest.fixture()
    def test_setup(self):
        global driver
        global wait
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        driver.get("http://dropoids.me/")
        wait = WebDriverWait(driver, 20)
        yield
        driver.close()
        driver.quit()

    def test_validsignup(self, test_setup):
        firstname = "eslam"
        lastname = "ashraf"
        age = "21"
        email = "eslam.zizo14@gmail.com"
        password = "Eslam4423415"
        driver.find_element_by_xpath("//a[contains(text(),'Sign up here')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='firstname']").send_keys(firstname)
        driver.find_element_by_xpath("//input[@id='lastname']").send_keys(lastname)
        driver.find_element_by_xpath("//input[@id='yourage']").send_keys(age)
        driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Signup']").click()
        time.sleep(5)
        assert (driver.current_url == "https://dropoids.me/")

    def test_emptylastname(self, test_setup):
        firstname = "eslam"
        age = "21"
        email = "eslam.zizo14@gmail.com"
        password = "Eslam4423415"
        driver.find_element_by_xpath("//a[contains(text(),'Sign up here')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='firstname']").send_keys(firstname)
        driver.find_element_by_xpath("//input[@id='yourage']").send_keys(age)
        driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Signup']").click()
        time.sleep(5)
        assert (driver.current_url != "https://dropoids.me/")

    def test_emptyage(self, test_setup):
        firstname = "eslam"
        lastname = "ashraf"
        email = "eslam.zizo14@gmail.com"
        password = "Eslam4423415"
        driver.find_element_by_xpath("//a[contains(text(),'Sign up here')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='firstname']").send_keys(firstname)
        driver.find_element_by_xpath("//input[@id='lastname']").send_keys(lastname)
        driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Signup']").click()
        time.sleep(5)
        assert (driver.current_url != "https://dropoids.me/")

    def test_emptymail(self, test_setup):
        firstname = "eslam"
        lastname = "ashraf"
        age = "21"
        password = "Eslam4423415"
        driver.find_element_by_xpath("//a[contains(text(),'Sign up here')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='firstname']").send_keys(firstname)
        driver.find_element_by_xpath("//input[@id='lastname']").send_keys(lastname)
        driver.find_element_by_xpath("//input[@id='yourage']").send_keys(age)
        driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Signup']").click()
        time.sleep(5)
        assert (driver.current_url != "https://dropoids.me/")

    def test_emptypass(self, test_setup):
        firstname = "eslam"
        lastname = "ashraf"
        age = "21"
        email = "eslam.zizo14@gmail.com"
        driver.find_element_by_xpath("//a[contains(text(),'Sign up here')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='firstname']").send_keys(firstname)
        driver.find_element_by_xpath("//input[@id='lastname']").send_keys(lastname)
        driver.find_element_by_xpath("//input[@id='yourage']").send_keys(age)
        driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        driver.find_element_by_xpath("//input[@value='Signup']").click()
        time.sleep(5)
        assert (driver.current_url != "https://dropoids.me/")

    def test_emptyfirstname(self, test_setup):
        lastname = "ashraf"
        age = "21"
        email = "eslam.zizo14@gmail.com"
        password = "Eslam4423415"
        driver.find_element_by_xpath("//a[contains(text(),'Sign up here')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='lastname']").send_keys(lastname)
        driver.find_element_by_xpath("//input[@id='yourage']").send_keys(age)
        driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Signup']").click()
        time.sleep(5)
        assert (driver.current_url != "https://dropoids.me/")

    def test_wrongfirstname(self, test_setup):
        firstname = "eslam@gmail.com"
        lastname = "ashraf"
        age = "21"
        email = "esladwededswm.zizo14@gmail.com"
        password = "Eslam4423415"
        driver.find_element_by_xpath("//a[contains(text(),'Sign up here')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='firstname']").send_keys(firstname)
        driver.find_element_by_xpath("//input[@id='lastname']").send_keys(lastname)
        driver.find_element_by_xpath("//input[@id='yourage']").send_keys(age)
        driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Signup']").click()
        driver.find_element_by_xpath("//input[@value='Signup']").click()
        time.sleep(5)
        assert (driver.current_url != "https://dropoids.me/")

    def test_wronglastname(self, test_setup):
        firstname = "eslam"
        lastname = "ashraf@gmail.com"
        age = "21"
        email = "eslaewqwqeqem.zizo14@gmail.com"
        password = "Eslam4423415"
        driver.find_element_by_xpath("//a[contains(text(),'Sign up here')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='firstname']").send_keys(firstname)
        driver.find_element_by_xpath("//input[@id='lastname']").send_keys(lastname)
        driver.find_element_by_xpath("//input[@id='yourage']").send_keys(age)
        driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Signup']").click()
        driver.find_element_by_xpath("//input[@value='Signup']").click()
        time.sleep(5)
        assert (driver.current_url != "https://dropoids.me/")

    def test_invalidage(self, test_setup):
        firstname = "eslam"
        lastname = "ashraf"
        age = "9"
        email = "eslam.zizo14@gmail.com"
        password = "Eslam4423415"
        driver.find_element_by_xpath("//a[contains(text(),'Sign up here')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='firstname']").send_keys(firstname)
        driver.find_element_by_xpath("//input[@id='lastname']").send_keys(lastname)
        driver.find_element_by_xpath("//input[@id='yourage']").send_keys(age)
        driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Signup']").click()
        time.sleep(5)
        assert (driver.current_url != "https://dropoids.me/")

    def test_invalidageandpass(self, test_setup):
        firstname = "eslam"
        lastname = "ashraf"
        age = "9"
        email = "eslam.zizo14@gmail.com"
        password = "Es"
        driver.find_element_by_xpath("//a[contains(text(),'Sign up here')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='firstname']").send_keys(firstname)
        driver.find_element_by_xpath("//input[@id='lastname']").send_keys(lastname)
        driver.find_element_by_xpath("//input[@id='yourage']").send_keys(age)
        driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Signup']").click()
        time.sleep(5)
        assert (driver.current_url != "https://dropoids.me/")

    def test_spacefirstname(self, test_setup):
        firstname = "  "
        lastname = "ashraf"
        age = "21"
        email = "eslam.zizo14@gmail.com"
        password = "Eslam4423415"
        driver.find_element_by_xpath("//a[contains(text(),'Sign up here')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='firstname']").send_keys(firstname)
        driver.find_element_by_xpath("//input[@id='lastname']").send_keys(lastname)
        driver.find_element_by_xpath("//input[@id='yourage']").send_keys(age)
        driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Signup']").click()
        time.sleep(5)
        assert (driver.current_url != "https://dropoids.me/")

    def test_spacelastname(self, test_setup):
        firstname = "eslam"
        lastname = "  "
        age = "21"
        email = "eslam.zizo14@gmail.com"
        password = "Eslam4423415"
        driver.find_element_by_xpath("//a[contains(text(),'Sign up here')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='firstname']").send_keys(firstname)
        driver.find_element_by_xpath("//input[@id='lastname']").send_keys(lastname)
        driver.find_element_by_xpath("//input[@id='yourage']").send_keys(age)
        driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Signup']").click()
        time.sleep(5)
        assert (driver.current_url != "https://dropoids.me/")

    def test_spaceage(self, test_setup):
        firstname = "eslam"
        lastname = "ashraf"
        age = "  "
        email = "eslam.zizo14@gmail.com"
        password = "Eslam4423415"
        driver.find_element_by_xpath("//a[contains(text(),'Sign up here')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='firstname']").send_keys(firstname)
        driver.find_element_by_xpath("//input[@id='lastname']").send_keys(lastname)
        driver.find_element_by_xpath("//input[@id='yourage']").send_keys(age)
        driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Signup']").click()
        time.sleep(5)
        assert (driver.current_url != "https://dropoids.me/")

    def test_spacemail(self, test_setup):
        firstname = "eslam"
        lastname = "ashraf"
        age = "21"
        email = "  "
        password = "Eslam4423415"
        driver.find_element_by_xpath("//a[contains(text(),'Sign up here')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='firstname']").send_keys(firstname)
        driver.find_element_by_xpath("//input[@id='lastname']").send_keys(lastname)
        driver.find_element_by_xpath("//input[@id='yourage']").send_keys(age)
        driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Signup']").click()
        time.sleep(5)
        assert (driver.current_url != "https://dropoids.me/")

    def test_spacepass(self, test_setup):
        firstname = "eslam"
        lastname = "ashraf"
        age = "21"
        email = "eslam.zizo14@gmail.com"
        password = "  "
        driver.find_element_by_xpath("//a[contains(text(),'Sign up here')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='firstname']").send_keys(firstname)
        driver.find_element_by_xpath("//input[@id='lastname']").send_keys(lastname)
        driver.find_element_by_xpath("//input[@id='yourage']").send_keys(age)
        driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Signup']").click()
        time.sleep(5)
        assert (driver.current_url != "https://dropoids.me/")

