from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HiddenLayersPage:

    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver

    def click_hidden_button(self) -> None:
        self.web_driver.find_element(By.ID, "greenButton").click()

    def click_button_twice(self, timeout=5) -> WebDriverWait:
        return WebDriverWait(self.web_driver, timeout).until(EC.presence_of_element_located((By.ID, "blueButton")))




