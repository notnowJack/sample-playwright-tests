import pytest
from playwright.sync_api import Page
from .helpers import has_login_field_error_message_appeared

def test_login_popup_appears(page: Page):
    page.goto("https://find.data.gov.scot/")
    page.get_by_text('Login').click()
    page.get_by_role('button', name='Log In').click()

    checkEmail = has_login_field_error_message_appeared(page, "Required field")
    checkPassword = has_login_field_error_message_appeared(page, "Required field", 1)
    # Check if both login popup elements are visible
    assert (checkEmail and checkPassword) is True