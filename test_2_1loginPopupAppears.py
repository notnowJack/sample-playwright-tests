import pytest
from playwright.sync_api import Page
from .helpers import has_login_popup_appeared

def test_login_popup_appears(page: Page):
    page.goto("https://find.data.gov.scot/")
    page.get_by_text('Login').click() 
    # Check if both login popup elements are visible
    both_visible = has_login_popup_appeared(page)
    assert both_visible is True