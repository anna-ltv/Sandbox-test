# Checking transition to the domains page, work of the buttons on the page and deletion of the created record

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

def test_open_domains_page():
    # Click the main menu button and go to Domains page
    pytest.driver.find_element_by_css_selector('.full').click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-menu-xmlid="website_x.menu_website_websites_list"]'))).click()

def test_create_discard_buttons():
    pytest.driver.find_element_by_css_selector('.full').click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-menu-xmlid="website_x.menu_website_websites_list"]'))).click()
    # Testing Create button
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn.btn-primary.o_list_button_add'))).click()
    # checking discard button
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn.btn-secondary.o_form_button_cancel'))).click()

def test_create_save_new_record():
    pytest.driver.find_element_by_css_selector('.full').click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-menu-xmlid="website_x.menu_website_websites_list"]'))).click()
    # Testing Create button
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn.btn-primary.o_list_button_add'))).click()
    # fill in the form with data
    sleep(2)
    domain_name = WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="domain"]')))
    domain_name.click()
    sleep(1.5)
    domain_name.send_keys('test_selenium_domain')
    sleep(1.5)
    # press save button
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[accesskey="s"]'))).click()

def test_checking_add_404_page_button():
    pytest.driver.find_element_by_css_selector('.full').click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-menu-xmlid="website_x.menu_website_websites_list"]'))).click()
    sleep(1.5)
    # Find the last element in the table and click Add 404 button, then click Discard
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//tr[last()]/td[14]/button[1]'))).click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn.btn-secondary.o_form_button_cancel'))).click()

def test_checking_edit_website_button():
    pytest.driver.find_element_by_css_selector('.full').click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-menu-xmlid="website_x.menu_website_websites_list"]'))).click()
    sleep(1.5)
    # Find the last element in the table and click Edit website button
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//tr[last()]/td[14]/button[3]'))).click()

def test_checking_open_at_domain_button():
    pytest.driver.find_element_by_css_selector('.full').click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-menu-xmlid="website_x.menu_website_websites_list"]'))).click()
    sleep(1.5)
    # Find the last element in the table and click Open at domain button
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//tr[last()]/td[14]/button[4]'))).click()

def test_checking_copy_website_button():
    pytest.driver.find_element_by_css_selector('.full').click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-menu-xmlid="website_x.menu_website_websites_list"]'))).click()
    sleep(1.5)
    # Find the last element in the table and click Copy Website button
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//tr[last()]/td[14]/button[5]'))).click()

def test_checking_add_scripts_button():
    pytest.driver.find_element_by_css_selector('.full').click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-menu-xmlid="website_x.menu_website_websites_list"]'))).click()
    sleep(1.5)
    # Find the last element in the table and click Add scripts button
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//tr[last()]/td[14]/button[6]'))).click()

def test_checking_pick_theme_button():
    pytest.driver.find_element_by_css_selector('.full').click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-menu-xmlid="website_x.menu_website_websites_list"]'))).click()
    sleep(1.5)
    # Find the last element in the table and click Pick a theme button
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//tr[last()]/td[14]/button[8]'))).click()

def test_cancel_deletion_of_record():
    pytest.driver.find_element_by_css_selector('.full').click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-menu-xmlid="website_x.menu_website_websites_list"]'))).click()
    sleep(1.5)
    # Find the last element in the table and click on the box
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//tr[last()]/td[1]/div'))).click()
    # Click Action button and choose Delete in the drop-down menu
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Action"]'))).click()
    sleep(1.5)
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Delete'))).click()
    sleep(1.5)
    # Confirm delete by pressing Cancel
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Cancel"]'))).click()


def test_delete_record():
    pytest.driver.find_element_by_css_selector('.full').click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-menu-xmlid="website_x.menu_website_websites_list"]'))).click()
    sleep(1.5)
    if pytest.driver.find_element_by_xpath('//tr[last()]/td[3]/a').text == 'test_selenium_domain':
        # Find the last element in the table and click on the box
        WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//tr[last()]/td[1]/div'))).click()
        # Click Action button and choose Delete in the drop-down menu
        WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Action"]'))).click()
        sleep(1.5)
        WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Delete'))).click()
        sleep(1.5)
        # Confirm delete by pressing ok
        WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Ok"]'))).click()
    else:
        pytest.xfail('Program cannot find the record created for this test. Check if "create new record" test passed')