#IMDB POM

# This code is used to import  the datas
import pytest

from Data import data
from Locator import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestNameSearch:
    # Setup before testing
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(data.WebData().url) # this code is used to get the url from the data
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10) # this code is used to for explicit wait
        yield
        # Teardown after testing
        self.driver.quit()
    def clickButton(self,locator):
        self.wait.until(ec.presence_of_element_located((By.XPATH,locator))).click()

    def fillText(self, locator,value):
        self.wait.until(ec.presence_of_element_located((By.XPATH, locator))).send_keys(value)
    def CLASSNAME(self, locator,value):
        self.wait.until(ec.presence_of_element_located((By.CLASS_NAME, locator))).send_keys(value)

    def test_fillForm(self,boot):
        #this promotes Scroll function
        self.driver.execute_script('window.scrollBy(0, 800)')
        #this will click the expand all
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, locator.WebLocator().expandAllLocator))).click()
        #This will send keys
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.ID,locator.WebLocator().nameLocator))).send_keys(
                data.WebData().name)
        #this will send the dob
        self.wait.until(ec.presence_of_element_located((By.ID, locator.WebLocator().birthdayLocator))).send_keys(
                data.WebData().birthday)
        self.driver.execute_script('window.scrollBy(0, 800)')
        self.wait.until(ec.presence_of_element_located((By.ID, locator.WebLocator().dbLocator))).send_keys(
                data.WebData().db)
        self.driver.execute_script('window.scrollBy(800, 0)')
        # variable declaration to search results
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH,locator.WebLocator().resultLocator)))












