from typing import Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement



class PageElement:

    def __init__(self, web_driver: WebDriver, locator: Tuple[str, str]):
        self.web_driver = web_driver
        self.locator = locator

    def _get_el(self) -> WebElement:
        return self.web_driver.find_element(*self.locator)

    def click(self) -> None:
        self._get_el().click()

    def send_keys(self, value: str) -> None:
        self.web_driver.find_element(*self.locator).send_keys(value)


