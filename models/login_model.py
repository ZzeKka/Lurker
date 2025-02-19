from playwright.sync_api import TimeoutError
from models.page import Page

import logging
import random

page_url = "https://www.linkedin.com/"

class LoginModel(Page):
    def __init__(self, page):
        # page
        super().__init__(page)
        self.page_url = page_url
        # locators
        self.sign_in_button = None
        self.sign_in_box = None
        self.username = None
        self.password = None
        self.new_sign_in_button = None
        
    def log_in(self):
        try:
            # Go to Sign In Page
            self.page.wait_for_timeout(random.uniform(3,5))
            self.sign_in_button = self.page.get_by_text("Sign in").and_(self.page.locator("[class*='nav__button-secondary btn-secondary-emphasis']"))
            self.sign_in_button.wait_for(timeout=10000)
            self.sign_in_button.click()
            # Sign In
            self.sign_in_box = self.page.locator('div.card-layout')
            self.sign_in_box.wait_for()
            # and_() dons't work with locator + get_by_role
            self.page.wait_for_timeout(random.uniform(3,5))
            self.username = self.page.locator('input#username')
            self.username.fill('jacintoobiquel@gmail.com')
            self.page.wait_for_timeout(random.uniform(3,5))
            self.password = self.page.locator('input#password')
            self.password.fill('JD*()DH72f39noicwcw')
            self.page.wait_for_timeout(random.uniform(3,5))
            self.new_sign_in_button = self.page.get_by_label('Sign in').and_(self.page.get_by_text('Sign in'))
            self.new_sign_in_button.click()        
        except TimeoutError as e:
            logging.error(f"Page timeout before clicking Sign In Button: {e}")
            raise
        except Exception as e:
            logging.error(f"Exception {e} fou  nd when trying to click on Sign In Button")
            raise