import pytest
from playwright.sync_api import Page
from .helpers import is_login_popup_complete

def test_login_popup_complete(page: Page):
    page.goto("https://find.data.gov.scot/")
    page.get_by_text('Login').click()

    # Check if both login popup elements are visible
    all_visible = is_login_popup_complete(page)
    assert all_visible is True