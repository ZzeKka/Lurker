from models.page import Page
import logging
import random
import time
page_url = "https://www.linkedin.com/jobs/"

class JobSearchModel(Page):
    def __init__(self, page):
        super().__init__(page)
        self.page_url = page_url
        self.country = None
        #locators
        self.locator_search_job = None
        self.locator_search_country = None

    def search_jobs_for_country(self, country_name :str, job_titles :tuple):
        #try:
            self.country = country_name
            self.navigate()
            # Visit the job search page for the country (LinkedIn job search interface)
            for job_title in job_titles: 
                # Fill Search Parameters
                self.locator_search_job = self.page.locator('input[role="combobox"][aria-label="Search by title, skill, or company"]')
                self.locator_search_job.fill(job_title)
                self.locator_search_country = self.page.locator('[role="combobox"][aria-label="City, state, or zip code"]')     
                self.locator_search_country.fill(country_name)
                self.page.wait_for_timeout(random.uniform(1,10))
                self.locator_search_country.press("Enter")
                
                job_elements = self.page.locator("a[class*='job-card-container__link']")
                #job_elements = self.page.locator("div[class*='job-card-container--clickable']")
                job_elements.highlight()
                self.page.pause()
                """

                # Find all job elements listed
                job_elements = self.page.locator("ul.jobs-search__results-list li")
                print(job_elements)
                job_count = job_elements.count()

                # Open a new tab for each job matching the title
                for i in range(job_count):
                    job_name = job_elements.nth(i).locator("h3").inner_text()
                    if job_title.lower() in job_name.lower():  # Case-insensitive match
                        job_link = job_elements.nth(i).locator("a").get_attribute("href")
                        print(f"Found job: {job_name}, opening {job_link}...")
                        
                        # Open a new tab with the job link
                        new_tab = self.page.context.new_page()
                        new_tab.goto(job_link)
                        time.sleep(2)  # Adding a slight delay to avoid overloading requests
            """

        #except Exception as e:
            #logging.error(f"Error while processing {country_name}: {str(e)}")
        