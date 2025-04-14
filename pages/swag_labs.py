from pages.base_page import BasePage
from components.components import WebElement

class SwagLabs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://www.saucedemo.com/'
        super().__init__(driver, self.base_url)

        self.input_name = WebElement(driver, 'input[id="user-name"]')
        self.input_password = WebElement(driver, 'input[id="password"]')
        self.icon = WebElement(driver, 'div.login_logo')
