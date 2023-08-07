from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class ClassAttributePage:

    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver

    def click_class_button(self) -> None:
        self.web_driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()



