from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class DynamicButtonPage:

    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver

    def click_dynamic_button(self) -> None:
        self.web_driver.find_element(By.CLASS_NAME, "btn.btn-primary").click()


