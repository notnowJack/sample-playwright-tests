
import pytest
from playwright.sync_api import Page
from .helpers import is_on_start_page

def test_start_page_check(page: Page):
	page.goto("https://find.data.gov.scot/")
	both_visible = is_on_start_page(page)
	assert both_visible is True
