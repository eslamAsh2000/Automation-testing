import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Tools.Baseclass import baseclass
from PageObjects.Mainpage import Mainpage
from PageObjects.loginpage import loginpage


class Testlogin():
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

    def test_valid(self, test_setup):
        email = "Admin@gmail.com"
        password = "1234"
        driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        element.send_keys(password)
        signing = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]")))
        signing.click()
        driver.maximize_window()
        time.sleep(3)
        assert (driver.current_url == "https://dropoids.me/user")

    def test_emptypassword(self, test_setup):
        email = "Admin@gmail.com"
        driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        signing = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]")))
        signing.click()
        driver.maximize_window()
        time.sleep(3)
        assert (driver.current_url != "https://dropoids.me/user")

    def test_emptymail(self, test_setup):
        password = "1234"
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        element.send_keys(password)
        signing = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]")))
        signing.click()
        driver.maximize_window()
        time.sleep(3)
        assert (driver.current_url == "https://dropoids.me/sign-up")

    def test_empty(self, test_setup):
        signing = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]")))
        signing.click()
        driver.maximize_window()
        time.sleep(3)
        assert (driver.current_url != "https://dropoids.me/user")

    def test_wrongpass(self, test_setup):
        email = "Admin@gmail.com"
        password = "12334"
        driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        element.send_keys(password)
        signing = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]")))
        signing.click()
        driver.maximize_window()
        time.sleep(3)
        assert (driver.current_url == "https://dropoids.me/sign-up")

    def test_wrong(self, test_setup):
        email = "Admiiin@gmail.com"
        password = "1234"
        driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        element.send_keys(password)
        signing = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]")))
        signing.click()
        driver.maximize_window()
        time.sleep(3)
        assert (driver.current_url == "https://dropoids.me/sign-up")

    def test_wrongmail(self, test_setup):
        email = "Admiiin"
        password = "1234"
        driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        element.send_keys(password)
        signing = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]")))
        signing.click()
        driver.maximize_window()
        time.sleep(3)
        assert (driver.current_url != "https://dropoids.me/user")

    def test_wrongpass(self, test_setup):
        email = "Admiiin@gmail.com"
        password = "1234"
        driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        element.send_keys(password)
        signing = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]")))
        signing.click()
        driver.maximize_window()
        time.sleep(3)
        assert (driver.current_url == "https://dropoids.me/sign-up")

    def test_wrongmailemptypass(self, test_setup):
        email = "Admiiin"
        driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        signing = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]")))
        signing.click()
        driver.maximize_window()
        time.sleep(3)
        assert (driver.current_url != "https://dropoids.me/user")

    def test_spacepassyahoo(self, test_setup):
        email = "Admiiin@yahoo.com"
        password = "     "
        driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        element.send_keys(password)
        signing = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]")))
        signing.click()
        driver.maximize_window()
        time.sleep(3)
        assert (driver.current_url == "https://dropoids.me/sign-up")

    def test_spacepassgmail(self, test_setup):
        email = "Admin@gmail.com"
        password = "     "
        driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        element.send_keys(password)
        signing = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]")))
        signing.click()
        driver.maximize_window()
        time.sleep(3)
        assert (driver.current_url == "https://dropoids.me/sign-up")

    def test_spacemail(self, test_setup):
        email = "  "
        password = "1234"
        driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        element.send_keys(password)
        signing = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]")))
        signing.click()
        driver.maximize_window()
        time.sleep(3)
        assert (driver.current_url == "https://dropoids.me/sign-up")

