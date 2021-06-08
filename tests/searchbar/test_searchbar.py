import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from Tools.Baseclass import baseclass
from PageObjects.Mainpage import Mainpage
from PageObjects.loginpage import loginpage


class Testsearch():
    @pytest.fixture()
    def test_setup(self):
        global org
        global driver
        global wait
        email = "Admin@gmail.com"
        password = "1234"
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        driver.get("http://dropoids.me/")
        wait = WebDriverWait(driver, 20)
        driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        element.send_keys(password)
        signing = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]")))
        signing.click()
        driver.maximize_window()
        time.sleep(3)
        yield
        driver.close()
        driver.quit()

    def test_searchpeople(self, test_setup):
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/nav[1]/div[1]/div[3]/div[1]/input[1]").send_keys("fathy")
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/nav[1]/div[1]/div[3]/div[1]/input[1]").click()
        driver.find_element_by_xpath("//a[@href='/searchPeople/fathy']").click()
        time.sleep(5)
        assert (driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/a[1]/div[1]/div[2]/div[1]/div[1]/h6[1]").is_displayed() == True)

    def test_searchpeopleandclick(self, test_setup):
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/nav[1]/div[1]/div[3]/div[1]/input[1]").send_keys("fathy")
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/nav[1]/div[1]/div[3]/div[1]/input[1]").click()
        driver.find_element_by_xpath("//a[@href='/searchPeople/fathy']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/a[1]/div[1]/div[2]/div[1]/div[1]/h6[1]").click()
        time.sleep(5)
        assert(driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/h1[1]").is_displayed() == True)

    def test_searchgroup(self, test_setup):
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/nav[1]/div[1]/div[3]/div[1]/input[1]").send_keys("admin")
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/nav[1]/div[1]/div[3]/div[1]/input[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//a[@href='/searchGroup/admin']").click()
        time.sleep(5)
        assert (driver.current_url == "https://dropoids.me/searchGroup/admin")

    def test_searchemptypeople(self, test_setup):
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/nav[1]/div[1]/div[3]/div[1]/input[1]").send_keys("    ")
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/nav[1]/div[1]/div[3]/div[1]/input[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//a[@href='/searchPeople/    ']").click()
        time.sleep(5)
        assert (driver.current_url != "https://dropoids.me/searchPeople/")

    def test_searchemptygroup(self, test_setup):
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/nav[1]/div[1]/div[3]/div[1]/input[1]").send_keys("    ")
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/nav[1]/div[1]/div[3]/div[1]/input[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//a[@href='/searchGroup/    ']").click()
        time.sleep(5)
        assert (driver.current_url != "https://dropoids.me/searchGroup/")



