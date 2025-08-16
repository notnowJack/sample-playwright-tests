from playwright.sync_api import Page, expect

# Helper functions for playwright tests

# on the start page?
def is_on_start_page(page: Page) -> bool:
    visible1 = page.is_visible("text=Discover Scottish Public Data")
    visible2 = page.is_visible("text=Save time in data searches. Gain insights on quality and usage.")
    return visible1 and visible2

# has the login popup appeared?
def has_login_popup_appeared(page: Page) -> bool:
    button = page.get_by_role('button', name='Log In').is_visible()
    heading = page.get_by_role('heading', name='Log In').is_visible()
    return button and heading

#
def is_login_popup_complete(page: Page) -> bool:
    heading = page.get_by_role('heading', name='Log In').is_visible()
    login_options = page.is_visible("text=GoogleMicrosoftor")
    email_field = page.get_by_role('textbox', name='input field for E.g. jane.doe').is_visible()
    password_field = page.get_by_role('textbox', name='input field for Enter password').is_visible()
    unlock_account = page.get_by_text('Unlock account').is_visible()
    forgot_password = page.get_by_text('Forgot your password?').is_visible()
    remember_me = page.get_by_role('checkbox').is_visible()
    login_button = page.get_by_role('button', name='Log In').is_visible()
    sign_up = page.get_by_role('button', name='Sign up for free').is_visible()
    guest = page.get_by_role('button', name='Continue as a guest?').is_visible()
    return (heading and login_options and email_field and password_field and unlock_account and forgot_password and remember_me and login_button and sign_up and guest)

def has_login_field_error_message_appeared(page: Page, error_message: str, index: int = 0, bold: bool = True) -> bool:
    error = page.get_by_text(error_message).nth(index)
    expect(error).to_be_visible(timeout=5000)
    return bold

def has_incorrect_login_popup_appeared(page: Page) -> bool:
    # Python Playwright does not support .filter({ hasText: ... }) directly, so we use locator with text and nth
    popup = page.locator('div', has_text='Incorrect email or password.').nth(3)
    expect(popup).to_be_visible(timeout=5000)
    return True
