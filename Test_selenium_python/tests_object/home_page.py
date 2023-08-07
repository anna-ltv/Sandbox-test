from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from page_element import PageElement


class HomePage:
    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver


    def open(self) -> None:
        self.web_driver.get("http://uitestingplayground.com/")
        self.dynamic_button = PageElement(self.web_driver, (By.LINK_TEXT, "Dynamic ID"))
        self.class_attribute = PageElement(self.web_driver, (By.LINK_TEXT, "Class Attribute"))
        self.hidden_layers = PageElement(self.web_driver, (By.LINK_TEXT, "Hidden Layers"))

    def click_dynamic_button_link(self) -> None:
        self.dynamic_button.click()

    def click_class_attribute_link(self) -> None:
        self.class_attribute.click()

    def click_hidden_layers_link(self) -> None:
        self.hidden_layers.click()

