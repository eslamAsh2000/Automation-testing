import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Tools.Baseclass import baseclass
from PageObjects.Mainpage import Mainpage
from PageObjects.loginpage import loginpage


class Testextra():
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

    def test_logout(self, test_setup):
        driver.find_element_by_xpath("//button[contains(text(),'Logout')]").click()
        time.sleep(2)
        assert (driver.current_url == "https://dropoids.me/")

    def test_swipe(self,test_setup):
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/a[1]/button[1]/*[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/button[2]/span[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/button[1]/span[1]").click()
        time.sleep(2)
        assert (driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/img[1]").is_displayed() == False)

    def test_addtofavandshare(self,test_setup):
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/nav[1]/div[1]/div[3]/div[1]/input[1]").send_keys("tarek")
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/nav[1]/div[1]/div[3]/div[1]/input[1]").click()
        driver.find_element_by_xpath("//a[@href='/searchPeople/tarek']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/a[1]/div[1]/div[2]/div[1]/div[1]/h6[1]").click()
        time.sleep(5)
        fav = driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/ul[1]/div[1]/li[3]/*[1]")
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/img[1]").click()
        fav.click()
        time.sleep(5)
        assert(driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/img[1]").is_displayed() == False)

    def test_following(self,test_setup):

        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/nav[1]/div[1]/div[3]/div[1]/input[1]").send_keys("tarek")
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/nav[1]/div[1]/div[3]/div[1]/input[1]").click()
        driver.find_element_by_xpath("//a[@href='/searchPeople/tarek']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/a[1]/div[1]/div[2]/div[1]/div[1]/h6[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
        time.sleep(3)
        assert (driver.find_element_by_xpath("//button[contains(text(),'UnFollow')]").is_displayed() == True)

    def test_unfollowing(self,test_setup):

        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/nav[1]/div[1]/div[3]/div[1]/input[1]").send_keys("tarek")
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/nav[1]/div[1]/div[3]/div[1]/input[1]").click()
        driver.find_element_by_xpath("//a[@href='/searchPeople/tarek']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/a[1]/div[1]/div[2]/div[1]/div[1]/h6[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//button[contains(text(),'UnFollow')]").click()
        time.sleep(3)
        assert (driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").is_displayed() == True)

    def test_friendsviewandviewall(self,test_setup):
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/ul[1]/li[1]/a[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[contains(text(),'Friend view')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/ul[1]/li[1]/a[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[contains(text(),'View all')]").click()
        time.sleep(5)
        assert(driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/ul[1]/li[1]/a[1]").is_displayed() == False)



