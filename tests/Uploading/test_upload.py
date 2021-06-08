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


class Testupload():
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
        time.sleep(10)
        str1 = str(driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/p[1]").text)
        org = ''.join(filter(lambda i: i.isdigit(), str1))
        yield
        driver.close()
        driver.quit()

    def test_photo1jpg(self, test_setup):
        driver.find_element_by_xpath("//i[@class='flaticon-cloud-computing']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='file']").send_keys("C:\\EDoCKnkWsAE7Fbz.jpg")
        time.sleep(5)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/nav[1]/div[1]/div[1]/a[3]/button[1]").click()
        time.sleep(6)
        driver.refresh()
        time.sleep(10)
        str1 = str(driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/p[1]").text)
        r = ''.join(filter(lambda i: i.isdigit(), str1))
        assert (int(r) == int(org)+ 1)

    def test_photo2jpg(self, test_setup):
        driver.find_element_by_xpath("//i[@class='flaticon-cloud-computing']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='file']").send_keys("C:\\Users\\eslam\\Desktop\\jk.jpg")
        time.sleep(5)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/nav[1]/div[1]/div[1]/a[3]/button[1]").click()
        time.sleep(6)
        driver.refresh()
        time.sleep(10)
        str1 = str(driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/p[1]").text)
        r = ''.join(filter(lambda i: i.isdigit(), str1))
        assert (int(r) == int(org)+ 1)

    def test_photo3png(self, test_setup):
        driver.find_element_by_xpath("//i[@class='flaticon-cloud-computing']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='file']").send_keys("C:\\Users\\eslam\\Desktop\\test.png")
        time.sleep(5)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/nav[1]/div[1]/div[1]/a[3]/button[1]").click()
        time.sleep(6)
        driver.refresh()
        time.sleep(10)
        str1 = str(driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/p[1]").text)
        r = ''.join(filter(lambda i: i.isdigit(), str1))
        assert (int(r) == int(org)+ 1)

    def test_photo4png(self, test_setup):
        driver.find_element_by_xpath("//i[@class='flaticon-cloud-computing']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='file']").send_keys("C:\\Users\\eslam\\Desktop\\assign.png")
        time.sleep(5)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/nav[1]/div[1]/div[1]/a[3]/button[1]").click()
        time.sleep(6)
        driver.refresh()
        time.sleep(10)
        str1 = str(driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/p[1]").text)
        r = ''.join(filter(lambda i: i.isdigit(), str1))
        assert (int(r) == int(org)+ 1)

    def test_photo5png(self, test_setup):
        driver.find_element_by_xpath("//i[@class='flaticon-cloud-computing']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='file']").send_keys("C:\\Users\\eslam\\Desktop\\fio.png")
        time.sleep(5)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/nav[1]/div[1]/div[1]/a[3]/button[1]").click()
        time.sleep(6)
        driver.refresh()
        time.sleep(10)
        str1 = str(driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/p[1]").text)
        r = ''.join(filter(lambda i: i.isdigit(), str1))
        assert (int(r) == int(org)+ 1)

    def test_photo200kb(self, test_setup):
        driver.find_element_by_xpath("//i[@class='flaticon-cloud-computing']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='file']").send_keys("C:\\Users\\eslam\\Desktop\\test200kb.png")
        time.sleep(5)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/nav[1]/div[1]/div[1]/a[3]/button[1]").click()
        time.sleep(6)
        driver.refresh()
        time.sleep(10)
        str1 = str(driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/p[1]").text)
        r = ''.join(filter(lambda i: i.isdigit(), str1))
        assert (int(r) == int(org)+ 1)



