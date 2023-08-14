from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from page_element import PageElement

class TextInputPage:

    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver

    def enter_text(self, value: str) -> None:
        self.enter_text = PageElement(self.web_driver, (By.CLASS_NAME, "form-control")).send_keys(value)

    def change_button_name(self):
        self.web_driver.find_element(By.ID, "updatingButton").click()


