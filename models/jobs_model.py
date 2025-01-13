from models.page import Page
import logging
import time
page_url = "https://www.linkedin.com/jobs/"

class JobSearchModel(Page):
    def __init__(self, page):
        super().__init__(page)
        self.page_url = page_url
        self.country = None
        #locators

    def search_jobs_for_country(self, current_page : Page, country_name :str, job_titles :tuple):
        #try:
            self.country = country_name
            self.navigate()
            print(self.country)
            if self.country == 'Switzerland':
                self.page.pause()
            # Visit the job search page for the country (LinkedIn job search interface)
            for job_title in job_titles:                
                # Search for the job title
                   # search_box = self.page.locator()
                # search_box.fill(job_title)
                """
                # Select the location field and enter the country name
                location_box = self.page.locator("input[placeholder='Search location']")
                location_box.fill(country_name)
                # Trigger the search by pressing 'Enter' or clicking the search button
                search_box.press("Enter")
                self.page.wait_for_load_state("networkidle", timeout=15000)

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
        