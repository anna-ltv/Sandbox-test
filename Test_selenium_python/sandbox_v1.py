import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
  pytest.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
  pytest.driver.get("http://uitestingplayground.com/")

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

  assert WebDriverWait(pytest.driver, 5).until(EC.alert_is_present())  # checking the presence of alert popup
  pytest.driver.switch_to.alert.accept() # switch to alert

def test_hidden_layers():
  pytest.driver.find_element(By.LINK_TEXT, "Hidden Layers").click()
  assert "Hidden Layers" in pytest.driver.page_source # checking the presence of hidden layers title

  green_button = pytest.driver.find_element(By.ID, "greenButton")
  green_button.click()

  # Wait for the blue button to appear
  blue_button = WebDriverWait(pytest.driver, 7).until(EC.presence_of_element_located((By.ID, "blueButton")))
  blue_button.click()
  assert blue_button.is_enabled(), "The blue button should be clickable"

def test_click():
  pytest.driver.find_element(By.LINK_TEXT, "Click").click()
  assert "Click" in pytest.driver.page_source  # checking the presence of click title

  # Click the button
  first_click = pytest.driver.find_element(By.ID, "badButton")
  initial_class = first_click.get_attribute("class")  # Get the initial class attribute
  first_click.click()
  updated_class = first_click.get_attribute("class")  # Get the updated class attribute after clicking

  # Assert that the class has changed from "btn btn-primary" to "btn btn-success"
  assert initial_class == "btn btn-primary"
  assert updated_class == "btn btn-success"

def test_text_input():
  pytest.driver.find_element(By.LINK_TEXT, "Text Input").click()
  assert "Text Input" in pytest.driver.page_source  # checking the presence of text input title

  """enter a new button name in the field"""
  new_button_name = "New Button"
  input_field = pytest.driver.find_element(By.CLASS_NAME, "form-control")
  input_field.send_keys(new_button_name)

  """click the button to change name"""
  change_button_name = pytest.driver.find_element(By.ID, "updatingButton")
  change_button_name.click()

  """Assert the button name has been changed"""
  assert pytest.driver.find_element(By.ID, "updatingButton").text == new_button_name

def test_scrollbars():
  pytest.driver.find_element(By.LINK_TEXT, "Scrollbars").click()
  assert "Scrollbars" in pytest.driver.page_source  # checking the presence of Scrollbars title

  hiding_button = pytest.driver.find_element(By.CSS_SELECTOR, "#hidingButton")
  ActionChains(pytest.driver) \
    .scroll_to_element(hiding_button) \
    .perform()

  assert hiding_button.is_displayed(), """Check the button is visible"""
  hiding_button.click()

