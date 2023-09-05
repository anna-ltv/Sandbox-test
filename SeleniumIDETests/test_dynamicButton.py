# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDynamicButton():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_dynamicButton(self):
    # Home page is opened
    self.driver.get("http://uitestingplayground.com/home")
    self.driver.set_window_size(1102, 984)
    # Click on the Dynamic ID link on the main page
    self.driver.find_element(By.LINK_TEXT, "Dynamic ID").click()
    # Click on the button with dynamic id
    self.driver.find_element(By.XPATH, "//button[contains(.,\'Button with Dynamic ID\')]").click()
    # Click on the button with the dynamic id once again
    self.driver.find_element(By.XPATH, "//button[contains(.,\'Button with Dynamic ID\')]").click()

  