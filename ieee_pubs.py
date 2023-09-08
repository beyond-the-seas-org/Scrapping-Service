from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (make sure to specify the path to your WebDriver)
driver = webdriver.Chrome()

# Navigate to IEEE Xplore
driver.get('https://ieeexplore.ieee.org/')

# Find the search bar and enter the professor's name
search_bar = driver.find_element(By.ID, 'search-box-1')
professor_name = 'Graham Neubig'  # Replace with the professor's name
search_bar.send_keys(professor_name)
search_bar.send_keys(Keys.RETURN)

# Wait for search results to load
time.sleep(5)  # You can adjust the sleep time as needed

# Click on the first search result (assuming it's the professor's profile)
professor_profile_link = driver.find_element(By.CSS_SELECTOR,'.List-results-items a')
professor_profile_link.click()

# Wait for the professor's profile page to load
time.sleep(5)

# Scrape the publication details (title, abstract, keywords, doi, venue, publication date, citations)
publications = driver.find_elements(By.CSS_SELECTOR, '.List-results-items .description')
for publication in publications:
    title = publication.find_element(By.CSS_SELECTOR,'.title a').text
    abstract = publication.find_element(By.CSS_SELECTOR,'.abstract').text
    keywords = publication.find_element(By.CSS_SELECTOR,'.author-keywords .ng-binding').text
    doi = publication.find_element(By.CSS_SELECTOR,'.document-identifier .ng-binding').text
    venue = publication.find_element(By.CSS_SELECTOR,'.publisher-info-container .title').text
    publication_date = publication.find_element(By.CSS_SELECTOR,'.publisher-info-container .publication-date').text
    citations = publication.find_element(By.CSS_SELECTOR,'.societies .citation.ng-binding').text

    # Print or store the scraped data as needed
    print("Title:", title)
    print("Abstract:", abstract)
    print("Keywords:", keywords)
    print("DOI:", doi)
    print("Venue:", venue)
    print("Publication Date:", publication_date)
    print("Citations:", citations)
    print("\n")

# Close the browser
driver.quit()
