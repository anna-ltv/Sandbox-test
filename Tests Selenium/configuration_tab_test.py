# Checking buttons in Configuration tab: redirects, pages, settings, forms

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome()
    pytest.driver.implicitly_wait(10)
    pytest.driver.get('https://dev-test.tripmersion.com/web/login')
    pytest.driver.find_element_by_id('login').send_keys('admin')
    pytest.driver.find_element_by_id('password').send_keys('admin')
    pytest.driver.find_element_by_css_selector('.btn.btn-primary.btn-block').click()

    yield
    pytest.driver.quit()

def test_open_configuration_tab():
    # Open drop-down list of Configuration on Website page
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="website.menu_website_configuration"]').click()
    sleep(3)
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Configuration'))).click()

def test_select_settings_in_configuration():
    # Open drop-down list of Configuration on Website page
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="website.menu_website_configuration"]').click()
    sleep(3)
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Configuration'))).click()
    # Select Settings item
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-action-id="161"]'))).click()

def test_select_pages_in_configuration():
    # Open drop-down list of Configuration on Website page
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="website.menu_website_configuration"]').click()
    sleep(3)
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Configuration'))).click()
    # Select Pages item
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-action-id="150"]'))).click()

def test_select_redirects_in_configuration():
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="website.menu_website_configuration"]').click()
    sleep(3)
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Configuration'))).click()
    # Select Redirects
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-action-id="176"]'))).click()

def test_select_robotic_form_in_configuration():
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="website.menu_website_configuration"]').click()
    sleep(3)
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Configuration'))).click()
    # Select Robotic Form
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-action-id="175"]'))).click()


def test_select_feedback_form_in_configuration():
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="website.menu_website_configuration"]').click()
    sleep(3)
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Configuration'))).click()
    # Select Feedback Form
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-action-id="172"]'))).click()


def test_select_contacts_form_in_configuration():
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="website.menu_website_configuration"]').click()
    sleep(3)
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Configuration'))).click()
    # Select Contacts Form
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-action-id="173"]'))).click()


def test_select_arabic_form_in_configuration():
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="website.menu_website_configuration"]').click()
    sleep(3)
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Configuration'))).click()
    # Select Arabic Form
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-action-id="174"]'))).click()




