import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Tools.Baseclass import baseclass
from PageObjects.Mainpage import Mainpage
from PageObjects.loginpage import loginpage


class Testexplore():
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

    def test_explore(self, test_setup):
        driver.find_element_by_xpath("//a[contains(text(),'Explore')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/nav[1]/div[1]/div[1]/ul[1]/li[2]/ul[1]/li[1]/a[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/nav[1]/div[1]/div[1]/ul[1]/li[2]/ul[1]/li[2]/a[1]").click()
        time.sleep(5)
        assert (driver.find_element_by_xpath("//a[contains(text(),'You')]").is_displayed() == False)
