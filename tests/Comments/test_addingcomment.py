import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Tools.Baseclass import baseclass
from PageObjects.Mainpage import Mainpage
from PageObjects.loginpage import loginpage


class Testaddcomment():
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
        time.sleep(20)
        yield
        driver.close()
        driver.quit()

    def test_addcomment(self, test_setup):
        test = "test"
        driver.find_element_by_xpath(
            "//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/a[1]/button[1]/*[1]").click()
        time.sleep(20)
        str1 = str(driver.find_element_by_css_selector(
            "div.App div.imagePreview div.restPhotoDetails.container:nth-child(3) div.photoInteractions div:nth-child(2) > h4:nth-child(1)").text)
        org = ''.join(filter(lambda i: i.isdigit(), str1))
        element = driver.find_element_by_xpath("//input[@id='tag']")
        element.send_keys(test)
        driver.find_element_by_xpath("//button[contains(text(),'comment')]").click()
        time.sleep(5)
        driver.refresh()
        time.sleep(10)
        str2 = str(driver.find_element_by_css_selector(
            "div.App div.imagePreview div.restPhotoDetails.container:nth-child(3) div.photoInteractions div:nth-child(2) > h4:nth-child(1)").text)
        r = ''.join(filter(lambda i: i.isdigit(), str2))
        assert ((int(r) == int(org) + 1))

    def test_addcomment2(self, test_setup):
        test = "testwerwf"
        driver.find_element_by_xpath(
            "//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/a[1]/button[1]/*[1]").click()
        time.sleep(20)
        str1 = str(driver.find_element_by_css_selector(
            "div.App div.imagePreview div.restPhotoDetails.container:nth-child(3) div.photoInteractions div:nth-child(2) > h4:nth-child(1)").text)
        org = ''.join(filter(lambda i: i.isdigit(), str1))
        element = driver.find_element_by_xpath("//input[@id='tag']")
        element.send_keys(test)
        driver.find_element_by_xpath("//button[contains(text(),'comment')]").click()
        time.sleep(5)
        driver.refresh()
        time.sleep(10)
        str2 = str(driver.find_element_by_css_selector(
            "div.App div.imagePreview div.restPhotoDetails.container:nth-child(3) div.photoInteractions div:nth-child(2) > h4:nth-child(1)").text)
        r = ''.join(filter(lambda i: i.isdigit(), str2))
        assert ((int(r) == int(org) + 1))

    def test_addcomment3(self, test_setup):
        test = "testnow"
        driver.find_element_by_xpath(
            "//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/a[1]/button[1]/*[1]").click()
        time.sleep(20)
        str1 = str(driver.find_element_by_css_selector(
            "div.App div.imagePreview div.restPhotoDetails.container:nth-child(3) div.photoInteractions div:nth-child(2) > h4:nth-child(1)").text)
        org = ''.join(filter(lambda i: i.isdigit(), str1))
        element = driver.find_element_by_xpath("//input[@id='tag']")
        element.send_keys(test)
        driver.find_element_by_xpath("//button[contains(text(),'comment')]").click()
        time.sleep(5)
        driver.refresh()
        time.sleep(10)
        str2 = str(driver.find_element_by_css_selector(
            "div.App div.imagePreview div.restPhotoDetails.container:nth-child(3) div.photoInteractions div:nth-child(2) > h4:nth-child(1)").text)
        r = ''.join(filter(lambda i: i.isdigit(), str2))
        assert ((int(r) == int(org) + 1))

    def test_addemptycomment(self, test_setup):
        test = "  "
        driver.find_element_by_xpath(
            "//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/a[1]/button[1]/*[1]").click()
        time.sleep(20)
        str1 = str(driver.find_element_by_css_selector(
            "div.App div.imagePreview div.restPhotoDetails.container:nth-child(3) div.photoInteractions div:nth-child(2) > h4:nth-child(1)").text)
        org = ''.join(filter(lambda i: i.isdigit(), str1))
        element = driver.find_element_by_xpath("//input[@id='tag']")
        element.send_keys(test)
        driver.find_element_by_xpath("//button[contains(text(),'comment')]").click()
        time.sleep(5)
        driver.refresh()
        time.sleep(10)
        str2 = str(driver.find_element_by_css_selector(
            "div.App div.imagePreview div.restPhotoDetails.container:nth-child(3) div.photoInteractions div:nth-child(2) > h4:nth-child(1)").text)
        r = ''.join(filter(lambda i: i.isdigit(), str2))
        assert ((int(r) != int(org) + 1))

    def test_addcommentphstream(self, test_setup):
        test = "testcommenting"
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/img[1]").click()
        driver.find_element_by_xpath(
            "//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/ul[1]/div[1]/li[2]/*[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//textarea[@id='com']").send_keys(test)
        driver.find_element_by_xpath("//button[contains(text(),'Add comment')]").click()
        time.sleep(10)
        assert (driver.find_element_by_xpath("//p[contains(text(),'testcommenting')]").is_displayed() == True)
