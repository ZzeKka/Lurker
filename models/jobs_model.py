from structures.job_card import Job_Card
from models.page import Page
import logging
import random
import time

page_url = "https://www.linkedin.com/jobs/"

class JobSearchModel(Page):
    def __init__(self, page):
        super().__init__(page)
        self.country = None
        self.page_url = page_url
        #locators
        self.locator_search_job = None
        self.locator_search_country = None
        self.job_elements = None
        self.job_elements_scrollbar = None

    def search_jobs_for_country(self, country_name :str, job_titles :tuple):
        #try:
            self.country = country_name
            self.navigate()
            # Visit the job search page for the country (LinkedIn job search interface)
            for job_title in job_titles: 
                # Fill Search Parameters
                self.page.wait_for_timeout(random.uniform(2,6))
                self.locator_search_job = self.page.locator('input[role="combobox"][aria-label="Search by title, skill, or company"]')
                
                self.page.wait_for_timeout(random.uniform(2,6))
                self.locator_search_job.fill(job_title)
                self.locator_search_country = self.page.locator('[role="combobox"][aria-label="City, state, or zip code"]')     
                self.locator_search_country.fill(country_name)
                
                self.page.wait_for_timeout(random.uniform(2,6))
                self.locator_search_job.press("Enter")
                
                self.page.wait_for_timeout(random.uniform(2,6))
                self.job_elements_scrollbar = self.page.locator("div[class*='scaffold-layout__list '] > div")
                for _ in range(10):
                    self.job_elements_scrollbar.hover()
                    self.page.mouse.wheel(0, 250)
                    self.page.wait_for_timeout(random.uniform(5,10))

                #link locator  
                #self.job_elements = self.page.locator("a[class*='job-card-container__link'][class*='job-card-list']").all()
                
                self.job_elements = self.page.locator("div[class*='job-card-container--clickable']")
                self.job_elements.highlight()
                self.page.pause()
                #job_elements = self.page.locator("div[class*='job-card-container--clickable']")
                for job_element in self.job_elements:
                    job_element.highlight()
                    #job_title = job_element.locator("div > div[class*='job-card-list__entity']")
                    print(job_element.get_attribute("class"))
                    #job_title.highlight()
                    #> div[class*='entity-lockup__content'] > div > a > span[aria-hidden='true']
                    self.page.pause()
                    #job_card = Job_Card()
                    #how_long_posted
                    #application_link
                    
                # First get the right locator where you can extract attriutes (get_attribute) the easiest.
                # Ectract links from each locator
                # After That im gonna return a list of links which is gonna ned this method
                # Can also make a condition to not add certain links where the lemetn has a title that contains words like 'senior', 'associate', etc
                self.page.pause()
                                        

        #except Exception as e:
            #logging.error(f"Error while processing {country_name}: {str(e)}")
        