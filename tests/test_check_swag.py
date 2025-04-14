from pages.swag_labs import SwagLabs

def test_search_icon(browser):
    page = SwagLabs(browser)

    page.visit()
    assert page.exist_icon()

def test_search_login_input(browser):
    page = SwagLabs(browser)

    page.visit()
    assert page.find_element('input[id="user-name"]')

def test_search_password_input(browser):
    page = SwagLabs(browser)

    page.visit()
    assert page.find_element('input[id="password"]')