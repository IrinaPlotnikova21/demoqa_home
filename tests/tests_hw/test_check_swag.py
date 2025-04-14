from pages.swag_labs import SwagLabs

def test_search_icon(browser):
    page = SwagLabs(browser)

    page.visit()
    assert page.icon.exist()

def test_search_login_input(browser):
    page = SwagLabs(browser)

    page.visit()
    assert page.input_name.exist()

def test_search_password_input(browser):
    page = SwagLabs(browser)

    page.visit()
    assert page.input_password.exist()