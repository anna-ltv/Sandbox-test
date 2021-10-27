# Test checking possibilities of opening settings page, creation of a new website, canceling of creation of a website,
# opening of website page, entering and exiting editor mode, editing pages of the website, moving the website to archive
# deleting the website from archive

from selenium import webdriver
import pytest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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


def test_open_settings_page_website_tab():
    # Click the main menu button and go to Settings page, Website tab
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="base.menu_administration"]').click()
    pytest.driver.find_element_by_xpath('//span[text()="Website"]').click()

def test_open_window_create_new_website_in_settings():
    # Click the main menu button and go to Settings page, Website tab
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="base.menu_administration"]').click()
    pytest.driver.find_element_by_xpath('//span[text()="Website"]').click()
    # click Create a New Website button
    pytest.driver.find_element_by_xpath('//span[text()="Create a New Website"]').click()

def test_enter_website_name():
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="base.menu_administration"]').click()
    pytest.driver.find_element_by_xpath('//span[text()="Website"]').click()
    pytest.driver.find_element_by_xpath('//span[text()="Create a New Website"]').click()
    sleep(3)
    # enter some value in website name field
    website_name = WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="name"]')))
    website_name.click()
    website_name.send_keys('Test_Selenium_Website')

def test_cancel_creation_of_new_website():
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="base.menu_administration"]').click()
    pytest.driver.find_element_by_xpath('//span[text()="Website"]').click()
    pytest.driver.find_element_by_xpath('//span[text()="Create a New Website"]').click()
    sleep(3)
    # click cancel button
    pytest.driver.find_element_by_xpath('//span[text()="Cancel"]').click()

def test_create_new_website_in_settings():
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="base.menu_administration"]').click()
    pytest.driver.find_element_by_xpath('//span[text()="Website"]').click()
    pytest.driver.find_element_by_xpath('//span[text()="Create a New Website"]').click()
    sleep(3)
    # enter some value in website name field
    website_name = WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="name"]')))
    website_name.click()
    website_name.send_keys('Test_Selenium_Website')
    pytest.driver.find_element_by_name('create_and_redirect_to_theme').click()

def test_open_website_page_in_main_menu():
    # click main menu
    pytest.driver.find_element_by_css_selector('.full').click()
    # choose website button
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="website.menu_website_configuration"]').click()
    sleep(3)

def test_choose_website():
    # the program chooses the website from the list
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="website.menu_website_configuration"]').click()
    sleep(3)
    pytest.driver.find_element_by_xpath('//button[last()]').click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Go to Website'))).click()

def test_enter_edit_mode():
    # the program chooses the website from the list and clicks the Edit button
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="website.menu_website_configuration"]').click()
    sleep(3)
    pytest.driver.find_element_by_xpath('//button[last()]').click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Go to Website'))).click()
    edit_button = pytest.driver.find_element_by_css_selector('a[data-action="edit"]')
    edit_button.click()
    sleep(3)
    edit_button.send_keys(Keys.ENTER)

def test_exit_edit_mode():
    # the program chooses the website from the list, clicks the Edit button, waits till the edit mode is on and then presses discard
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="website.menu_website_configuration"]').click()
    sleep(3)
    pytest.driver.find_element_by_xpath('//button[last()]').click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Go to Website'))).click()
    edit_button = pytest.driver.find_element_by_css_selector('a[data-action="edit"]')
    edit_button.click()
    sleep(3)
    edit_button.send_keys(Keys.ENTER)
    sleep(10)
    pytest.driver.find_element_by_xpath('/html/body/div[3]/form/button[1]').click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Ok"]'))).click()


def test_open_pages_menu():
    # the program chooses the website from the list and opens pages menu
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="website.menu_website_configuration"]').click()
    time.sleep(3)
    pytest.driver.find_element_by_xpath('//button[last()]').click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Go to Website'))).click()
    pages_button = WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.ID, 'content-menu-button')))
    time.sleep(2)
    pages_button.click()

def test_open_edit_menu():
    # the program chooses the website from the list, opens pages menu and selects edit menu
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="website.menu_website_configuration"]').click()
    time.sleep(3)
    pytest.driver.find_element_by_xpath('//button[last()]').click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Go to Website'))).click()
    pages_button = WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.ID, 'content-menu-button')))
    pages_button.click()
    time.sleep(2)
    pages_button.click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-action="edit_menu"]'))).click()

def test_add_menu_item_to_pages():
    # the program chooses the website from the list, opens pages menu, selects edit menu, clicks add menu item
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="website.menu_website_configuration"]').click()
    time.sleep(3)
    pytest.driver.find_element_by_xpath('//button[last()]').click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Go to Website'))).click()
    pages_button = WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.ID, 'content-menu-button')))
    pages_button.click()
    time.sleep(2)
    pages_button.click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-action="edit_menu"]'))).click()
    time.sleep(5)
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Add Menu Item'))).click()


def test_save_new_menu_item():
    # the program chooses the website from the list, opens pages menu, selects edit menu, clicks add menu item, fills in the data and saves it
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="website.menu_website_configuration"]').click()
    time.sleep(3)
    pytest.driver.find_element_by_xpath('//button[last()]').click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Go to Website'))).click()
    pages_button = WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.ID, 'content-menu-button')))
    pages_button.click()
    time.sleep(2)
    pages_button.click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-action="edit_menu"]'))).click()
    time.sleep(7)
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Add Menu Item'))).click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.ID, 'o_link_dialog_label_input'))).send_keys('test_selenium')
    url_field = pytest.driver.find_element_by_id('o_link_dialog_url_input')
    url_field.send_keys('test_selenium.test')
    time.sleep(3)
    url_field.send_keys(Keys.TAB + Keys.ENTER)

def test_open_manage_pages():
    # the program chooses the website from the list, opens pages menu, selects manage pages option
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="website.menu_website_configuration"]').click()
    time.sleep(3)
    pytest.driver.find_element_by_xpath('//button[last()]').click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Go to Website'))).click()
    pages_button = WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.ID, 'content-menu-button')))
    pages_button.click()
    time.sleep(2)
    pages_button.click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[title="Manage Your Website Pages"]'))).click()

def test_activate_developer_mode_in_settings():
    # Click the main menu button and go to Settings page, choose Activate the developer mode in General Settings
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="base.menu_administration"]').click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Activate the developer mode'))).click()

def test_archive_website():
    # Click the main menu button and go to Settings page, choose Activate the developer mode in General Settings
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="base.menu_administration"]').click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Activate the developer mode'))).click()
    sleep(3)
    # Open drop-down list of Configuration on Website page
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="website.menu_website_configuration"]').click()
    sleep(2)
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Configuration'))).click()
    # Click Websites button in drop-down menu
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-action-id="149"]'))).click()
    sleep(2)
    if pytes.driver.find_element_by_xpath('//tr[last()]/td[2]').text == 'Test_Selenium_Website':
        # Choose the last element and archive it
        pytest.driver.find_element_by_xpath('//tr[last()]/td[1]/div').click()
        WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Action"]'))).click()
        WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Archive'))).click()
        # Confirm by pressing ok
        WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Ok"]'))).click()
    else:
        pytest.xfail("Program cannot find the record created for this test")

def test_set_filter_active_is_false():
    # Click the main menu button and go to Settings page, choose Activate the developer mode in General Settings
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="base.menu_administration"]').click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Activate the developer mode'))).click()
    sleep(2)
    # Open drop-down list of Configuration on Website page
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="website.menu_website_configuration"]').click()
    sleep(2)
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Configuration'))).click()
    # Click Websites button in drop-down menu
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-action-id="149"]'))).click()
    # Set filter Active-false and click Apply
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Filters"]'))).click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'o_add_custom_filter.dropdown-item'))).click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'o_input.o_generator_menu_operator'))).click()
    sleep(1.5)
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//option[text()="is false"]'))).click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn.btn-primary.o_apply_filter'))).click()


def test_delete_website_from_archive():
    # Click the main menu button and go to Settings page, choose Activate the developer mode in General Settings
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="base.menu_administration"]').click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Activate the developer mode'))).click()
    sleep(2)
    # Open drop-down list of Configuration on Website page
    pytest.driver.find_element_by_css_selector('.full').click()
    pytest.driver.find_element_by_css_selector('a[data-menu-xmlid="website.menu_website_configuration"]').click()
    sleep(2)
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Configuration'))).click()
    # Click Websites button in drop-down menu
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-action-id="149"]'))).click()
    # Set filter Active-false and click Apply
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Filters"]'))).click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'o_add_custom_filter.dropdown-item'))).click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'o_input.o_generator_menu_operator'))).click()
    sleep(1.5)
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//option[text()="is false"]'))).click()
    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn.btn-primary.o_apply_filter'))).click()
    if pytest.driver.find_element_by_xpath('//tr[last()]/td[2]').text == 'Test_Selenium_Website':
        # Choose the last element and delete it
        pytest.driver.find_element_by_xpath('//tr[last()]/td[1]/div').click()
        WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Action"]'))).click()
        WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Delete'))).click()
        # Cancel the deletion
        WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Cancel"]'))).click()
    else:
        pytest.xfail("Program cannot find the record created for this test. Check if 'create new website' test passed")





