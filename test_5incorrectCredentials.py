import pytest
from playwright.sync_api import Page
from .helpers import has_incorrect_login_popup_appeared

def test_login_popup_appears(page: Page):
    page.goto("https://find.data.gov.scot/")
    page.get_by_text('Login').click()

    page.get_by_role('textbox', name='input field for E.g. jane.doe').fill("invalid@user.com")
    page.get_by_role('textbox', name='input field for Enter password').fill("password")
    
    page.get_by_role('button', name='Log In').click()

    checkEmail = has_incorrect_login_popup_appeared(page)   
    assert checkEmail is True