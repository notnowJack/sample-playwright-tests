import pytest
from playwright.sync_api import Page
from .helpers import has_login_field_error_message_appeared

def test_login_popup_appears(page: Page):
    page.goto("https://find.data.gov.scot/")
    page.get_by_text('Login').click()

    page.get_by_role('textbox', name='input field for E.g. jane.doe').fill("abcdefgh@sharklasers.com")
    page.get_by_role('textbox', name='input field for Enter password').fill("invalid_password")
    
    page.get_by_role('button', name='Log In').click()
    
    error_element = page.get_by_text("You have made 1 of 5 incorrect login attempt(s).")
    not_bold = not ("font-weight" in error_element.evaluate("el => getComputedStyle(el).fontWeight") and int(error_element.evaluate("el => getComputedStyle(el).fontWeight")) >= 700)
    checkEmail = has_login_field_error_message_appeared(page, "You have made 1 of 5 incorrect login attempt(s).", 0, not_bold)

    assert checkEmail is True