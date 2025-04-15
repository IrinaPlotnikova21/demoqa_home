import time

from pages.accordion import Accordian

def test_visible_accordion(browser):
    page = Accordian(browser)

    page.visit()
    page.equal_url()

    assert page.section_1_head.exist()
    assert page.section_1_content.exist()

    assert page.section_1_content.is_visible()

    page.section_1_head.click()

    time.sleep(2)

    assert not page.section_1_content.is_visible()


def test_visible_accordion_default(browser):
    page = Accordian(browser)

    page.visit()
    page.equal_url()

    assert page.section_2_content_1.exist()
    assert not page.section_2_content_1.is_visible()

    assert page.section_2_content_2.exist()
    assert not page.section_2_content_2.is_visible()

    assert page.section_3_content.exist()
    assert not page.section_3_content.is_visible()