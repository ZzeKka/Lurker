import time
import random
from playwright.sync_api import sync_playwright, Playwright, TimeoutError
from models.login_model import LoginModel
from models.jobs_model import JobSearchModel
import logging
import re

linkedin_url = "https://www.linkedin.com/"
used_application = [] 

# Constant tuples
countries = ("Switzerland", "Portugal")
job_titles = ("Python Developer","Software Developer")

context_number = 0



def run(playwright: Playwright) -> None:
    chromium = playwright.chromium
    browser = chromium.launch(headless = False)
    context = browser.new_context()
    page = context.new_page()
    login_page = LoginModel(page)
    #Login and save cookies
    login_page.navigate()
    login_page.log_in()
    cookies = context.cookies()
    # Wait
    page.wait_for_timeout(3000)
    #for country in countries:
    for country in countries:
        country_context = browser.new_context()
        country_context.add_cookies(cookies)
        job_search_page = country_context.new_page()
        # Creating object responsibel for layout, locators, etc...
        job_search_page_modeled = JobSearchModel(job_search_page)
        job_search_page_modeled.search_jobs_for_country(country, job_titles)
        # Wait
        job_search_page.wait_for_timeout(random.uniform(1,10))

        


      
def main() -> None:
    with sync_playwright() as playwright:
        run(playwright)
        
if __name__ == '__main__':
    main()



