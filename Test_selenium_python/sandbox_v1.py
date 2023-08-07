import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
  pytest.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
  pytest.driver.get("http://uitestingplayground.com/")
  #driver.set_window_size(1920, 1040)

  yield
  pytest.driver.quit()

def test_dynamicbutton():
  pytest.driver.find_element(By.LINK_TEXT, "Dynamic ID").click()
  pytest.driver.find_element(By.CLASS_NAME, "btn.btn-primary").click()

  #assertions check the correct page and correct button name
  assert "Dynamic ID" in pytest.driver.page_source
  assert pytest.driver.find_element(By.CLASS_NAME, "btn.btn-primary").text == "Button with Dynamic ID"

def test_class_attribute():
  pytest.driver.find_element(By.LINK_TEXT, "Class Attribute").click()
  assert "Class Attribute" in pytest.driver.page_source  #checking the presence of class attribute title

  pytest.driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
  time.sleep(2)

  assert WebDriverWait(pytest.driver, 5).until(EC.alert_is_present()) #checking the presence of alert popup
  pytest.driver.switch_to.alert.accept() # switch to alert

def test_hidden_layers():
  pytest.driver.find_element(By.LINK_TEXT, "Hidden Layers").click()
  assert "Hidden Layers" in pytest.driver.page_source #checking the presence of hidden layers title

  green = pytest.driver.find_element(By.ID, "greenButton")
  green.click()
  WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.ID, "blueButton")))
#подумать над assert, чтобы проверять, что кнопка зеленая уже не доступна
