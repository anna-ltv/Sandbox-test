import time

from text_input_page import TextInputPage
from class_attribute_page import ClassAttributePage
from hidden_layers_page import HiddenLayersPage
from home_page import HomePage
from dynamic_button_page import DynamicButtonPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def testing():
  web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

  home_page = HomePage(web_driver)
  home_page.open()
  assert "UI Test Automation" in web_driver.page_source

  web_driver.quit()

def test_dynamicbutton():
  web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

  home_page = HomePage(web_driver)
  dynamic_button_page = DynamicButtonPage(web_driver)

  home_page.open()
  home_page.click_dynamic_button_link()

  assert "Dynamic ID" in web_driver.page_source  # checking the presence of dynamic id title

  dynamic_button_page.click_dynamic_button()
  assert web_driver.find_element(By.CLASS_NAME, "btn.btn-primary").text == "Button with Dynamic ID"  # check the button name

def test_class_attribute():
  web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

  home_page = HomePage(web_driver)
  home_page.open()
  home_page.click_class_attribute_link()
  assert "Class Attribute" in web_driver.page_source  # checking the presence of class attribute title

  class_attribute_page = ClassAttributePage(web_driver)
  class_attribute_page.click_class_button()
  time.sleep(2)

  assert WebDriverWait(web_driver, 5).until(EC.alert_is_present())  # checking the presence of alert popup
  web_driver.switch_to.alert.accept()  # switch to alert

def test_hidden_layers():
  web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

  home_page = HomePage(web_driver)
  home_page.open()
  home_page.click_hidden_layers_link()
  assert "Hidden Layers" in web_driver.page_source  # checking the presence of hidden layers title

  hidden_layers_page = HiddenLayersPage(web_driver)
  hidden_layers_page.click_hidden_button()
  hidden_layers_page.click_button_twice()

def test_input_text():
  web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

  home_page = HomePage(web_driver)
  home_page.open()
  home_page.click_text_input_link()
  assert "Text Input" in web_driver.page_source  # checking the presence of text input title

  text_input_page = TextInputPage(web_driver)
  value = "New button"
  text_input_page.enter_text(value)

  text_input_page.change_button_name()



