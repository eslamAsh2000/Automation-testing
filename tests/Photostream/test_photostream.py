import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Tools.Baseclass import baseclass
from PageObjects.Mainpage import Mainpage
from PageObjects.loginpage import loginpage
from selenium.webdriver.common.keys import Keys


class Testphotostream():
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

    def test_photostream3buttonsright(self, test_setup):
        driver.find_element_by_xpath("//li[contains(text(),'Photostream')]").click()
        time.sleep(2)
        driver.find_element_by_xpath(
            "//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/ul[1]/li[3]/button[1]/*[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath(
            "//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/ul[1]/li[4]/button[1]/*[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath(
            "//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/ul[1]/li[5]/button[1]/*[1]").click()
        time.sleep(2)
        assert (driver.find_element_by_xpath(
            "//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/a[1]/button[1]/*[1]").is_displayed() == False)

    def test_photostreameditthenclicks(self, test_setup):
        driver.find_element_by_xpath("//li[contains(text(),'Photostream')]").click()
        time.sleep(2)
        driver.find_element_by_xpath(
            "//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/ul[1]/li[2]/a[1]/button[1]/*[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[2]/img[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/img[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[4]/img[1]").click()
        assert (driver.find_element_by_xpath("//button[contains(text(),'Logout')]").is_displayed() == False)

    def test_photostreameditthendelete(self, test_setup):
        driver.find_element_by_xpath("//li[contains(text(),'Photostream')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/ul[1]/li[2]/a[1]/button[1]/*[1]").click()
        time.sleep(10)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[6]/img[1]").click()
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[6]/button[1]/*[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//button[@id='confirm']").click()
        time.sleep(2)
        driver.refresh()
        time.sleep(10)
        assert (driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[2]/div[1]/div[4]/img[1]").is_displayed() == False)

    def test_photostreameditphototitle(self, test_setup):
        driver.find_element_by_xpath("//li[contains(text(),'Photostream')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/ul[1]/li[2]/a[1]/button[1]/*[1]").click()
        time.sleep(10)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]").click()
        time.sleep(3)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/input[1]").send_keys(Keys.CONTROL + "a")
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/input[1]").send_keys(Keys.DELETE)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/input[1]").send_keys("title edited")
        driver.find_element_by_xpath("//button[contains(text(),'Done')]").click()
        time.sleep(10)
        assert (driver.find_element_by_xpath("//h1[contains(text(),'title edited')]").is_displayed() == True)

    def test_photostreameditphototitleempty(self, test_setup):
        driver.find_element_by_xpath("//li[contains(text(),'Photostream')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/ul[1]/li[2]/a[1]/button[1]/*[1]").click()
        time.sleep(10)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]").click()
        time.sleep(3)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/input[1]").send_keys(Keys.CONTROL + "a")
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/input[1]").send_keys(Keys.DELETE)
        driver.find_element_by_xpath("//button[contains(text(),'Done')]").click()
        time.sleep(10)
        assert (driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[4]/img[1]").is_displayed() == True)

    def test_photostreameditphototitlespace(self, test_setup):
        driver.find_element_by_xpath("//li[contains(text(),'Photostream')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/ul[1]/li[2]/a[1]/button[1]/*[1]").click()
        time.sleep(10)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]").click()
        time.sleep(3)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/input[1]").send_keys(Keys.CONTROL + "a")
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/input[1]").send_keys(Keys.DELETE)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/input[1]").send_keys("    ")
        driver.find_element_by_xpath("//button[contains(text(),'Done')]").click()
        time.sleep(10)
        assert (driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[4]/img[1]").is_displayed() == True)

    def test_photostreameditincameraroll(self, test_setup):
        driver.find_element_by_xpath("//li[contains(text(),'Photostream')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/ul[1]/li[2]/a[1]/button[1]/*[1]").click()
        time.sleep(10)
        driver.find_element_by_xpath("//a[@id='a2']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[1]/img[1]").click()
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[2]/img[1]").click()
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[3]/img[1]").click()
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[4]/img[1]").click()
        driver.find_element_by_xpath("//h3[@id='delete_option']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//button[@id='confirm']").click()
        time.sleep(3)
        assert (driver.find_element_by_xpath("//button[@id='confirm']").is_displayed() == False)


