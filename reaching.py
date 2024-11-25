from playwright.sync_api import sync_playwright, Playwright, TimeoutError

# Regex
import logging
import re

def run(playwright: Playwright) -> None:
    chromium = playwright.chromium
    browser = chromium.launch(headless = False)
    page = browser.new_page() 
    # Sign In on Linkedin
    try:
        page.goto("https://www.linkedin.com/")
        page.wait_for_load_state("networkidle", timeout=15000)
        sign_in_button = page.get_by_text("Sign in").and_(page.locator("[class*='nav__button-secondary btn-secondary-emphasis']"))
        print(sign_in_button)
        print(1)
        sign_in_button.wait_for(timeout=10000)
        print(2)
        sign_in_button.click()
        page.pause()
        print(3)
    except TimeoutError:
        logging.error("Page timeout before clicking Sign In Button")
    except Exception as e:
        logging.error(f"Exception {e} found when trying to click on Sign In Button")

    
    

def main() -> None:
    with sync_playwright() as playwright:
        run(playwright)
        

if __name__ == '__main__':
    main()