import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Tools.Baseclass import baseclass
from PageObjects.Mainpage import Mainpage
from PageObjects.loginpage import loginpage


class Testabout():
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

    def test_aboutandclickalbum(self, test_setup):
        driver.find_element_by_xpath("//li[contains(text(),'About')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[1]/i[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[4]/div[2]/div[1]/ul[1]/li[2]").click()
        time.sleep(8)
        assert (driver.find_element_by_xpath(
            "//body/div[@id='root']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/i[1]").is_displayed() == False)

    def test_aboutandclickupload(self, test_setup):
        driver.find_element_by_xpath("//li[contains(text(),'About')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[1]/i[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//li[contains(text(),'Upload')]").click()
        time.sleep(8)
        assert (driver.find_element_by_xpath(
            "//body/div[@id='root']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/i[1]").is_displayed() == False)

    def test_aboutandsearch(self, test_setup):
        driver.find_element_by_xpath("//li[contains(text(),'About')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[1]/i[1]").click()
        time.sleep(5)
        element = driver.find_element_by_xpath(
            "//body/div[@id='root']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/input[1]")
        element.send_keys("test")
        driver.find_element_by_xpath(
            "//body/div[@id='root']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/button[1]/i[1]").click()
        time.sleep(6)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/i[1]").click()
        time.sleep(3)
        assert (driver.find_element_by_xpath("//button[contains(text(),'Logout')]").is_displayed() == False)

    def test_aboutandselectphoto(self, test_setup):
        driver.find_element_by_xpath("//li[contains(text(),'About')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[1]/i[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//button[contains(text(),'select')]").click()
        time.sleep(8)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/i[1]").click()
        time.sleep(4)
        assert (driver.find_element_by_xpath("//button[contains(text(),'Logout')]").is_displayed() == False)

    def test_aboutandfollowingorfollowersall(self, test_setup):
        driver.find_element_by_xpath("//li[contains(text(),'About')]").click()
        time.sleep(2)
        driver.find_element_by_xpath(
            "//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[1]/a[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//select[@id='sortForm']").click()
        driver.find_element_by_xpath("//option[contains(text(),'Following')]").click()
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/select[1]/option[3]").click()
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/select[1]/option[4]").click()
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//option[contains(text(),'Freinds and Family')]").click()
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]").click()
        time.sleep(2)
        element = driver.find_element_by_css_selector("#searchForm")
        element.send_keys("tarek")
        time.sleep(5)
        assert (driver.find_element_by_xpath("//button[contains(text(),'Logout')]").is_displayed() != True)
