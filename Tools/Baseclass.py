import pytest
import logging
import inspect
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class baseclass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger
    def verifyLink(self, text):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, text)))

    def verifyCSS(self, text):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, text)))

    def verifyXPATH(self, text):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, text)))


