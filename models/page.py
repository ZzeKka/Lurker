from playwright.sync_api import TimeoutError
import logging
import random

class Page:
    def __init__(self, page):
        # Object is the general page
        self.page = page 
    
    def navigate(self):
        """Navigate specific page to a current url"""
        try:
            self.page.wait_for_timeout(random.uniform(4,6))
            self.page.goto(self.page_url)
            self.page.wait_for_load_state("domcontentloaded", timeout=50000)
            print('Successfully entered in page_url')
        except TimeoutError as e:
            logging.error(f"Timeout error when navigating to {self.page_url}: {e}")
            raise
        except Exception as e:
            logging.error(f"Error while navigating to {self.page_url}: {e}")
            raise
    
    def wait_for_element(self, locator):
        try:
            """Wait for an element to appear on the page"""
            self.page.locator(locator).wait_for(timeout = 10000)
        except TimeoutError as e:
            logging.error(f"Element: {locator} not found, Timeout Exception: {e}")
            raise

    def get_page_url(self):
        """Get the current page url"""
        return self.page.url