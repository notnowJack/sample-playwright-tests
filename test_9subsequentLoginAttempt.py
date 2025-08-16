import pytest
from playwright.sync_api import Page
from .helpers import has_login_field_error_message_appeared

def test_login_popup_appears(page: Page):
    page.goto("https://find.data.gov.scot/")
    page.get_by_text('Login').click()

    page.get_by_role('textbox', name='input field for E.g. jane.doe').fill("a@a.com")
    page.get_by_role('textbox', name='input field for Enter password').fill("invalid_password")
    
    page.get_by_role('button', name='Log In').click()

    checkEmail = has_login_field_error_message_appeared(page, "Your account is locked,")   
    assert checkEmail is True