# Checking login and logout. Test steps:
# open login page -> fill in email -> fill in password -> click Log in button -> click on the profile button -> click Log out button -> quit

from time import sleep
from selenium import webdriver
import pytest

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome()
    pytest.driver.implicitly_wait(10)
    pytest.driver.get('https://dev-test.tripmersion.com/web/login')

    yield
    pytest.driver.quit()

def test_login():
    # Fill in user's email ID
    pytest.driver.find_element_by_id('login').send_keys('admin')
    # Fill in password
    pytest.driver.find_element_by_id('password').send_keys('admin')
    # Click the button to log in
    pytest.driver.find_element_by_css_selector('.btn.btn-primary.btn-block').click()

def test_log_out():
    test_login()
    # Open drop-down menu of Administrator
    sleep(3)
    pytest.driver.find_element_by_class_name('oe_topbar_name').click()
    # Select log out button
    pytest.driver.find_element_by_xpath('/html/body/header/nav/ul[3]/li[3]/div/a[6]').click()




