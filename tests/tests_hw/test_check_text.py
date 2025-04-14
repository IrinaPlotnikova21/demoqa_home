from pages.demo_qa import DemoQa
from pages.elements_page import ElementsPage

def test_search_by_home_page(browser):
    page = DemoQa(browser)

    page.visit()
    page.equal_url()

    page.footer.exist()

    text_footer = page.footer.get_text()
    text_valid = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

    assert text_footer == text_valid

def test_search_text_by_elements_page(browser):
    home_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    home_page.visit()
    home_page.equal_url()

    home_page.btn_elements.exist()
    home_page.btn_elements.click()

    elements_page.equal_url()

    elements_page.center_container.exist()

    text_footer = elements_page.center_container.get_text()
    text_valid = 'Please select an item from left to start practice.'

    assert text_footer == text_valid