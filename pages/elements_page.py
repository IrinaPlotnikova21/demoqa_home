from pages.base_page import BasePage
from components.components import WebElement

class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.center_container = WebElement(driver, '#app > div > div > div > div:nth-child(2)')