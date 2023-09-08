from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# Initialize a Selenium webdriver (adjust the path to your WebDriver executable)
driver = webdriver.Chrome()

# Read data from the JSON file
with open("faculty_info.json", "r", encoding="utf-8") as data_file:
    dataset = json.load(data_file)

# Create a dictionary to store faculty names and their respective publication links
faculty_publications = {}
faculty_data_list = []

# Open the IEEE Xplore website
driver.get("https://ieeexplore.ieee.org/")

# Iterate through faculty names and search for their publications

for data in dataset:
    faculty_name = data["name"]
    university = data["university"]
    image = data["image"]
    website = data["website"]
    research_interests = data["research_interests"]

    # Build the search query URL for IEEE Xplore
    search_query = f"https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=({faculty_name})+AND+({university})&highlight=true&returnFacets=ALL&returnType=SEARCH&matchPubs=true&ranges=2010_2023_Year&pageNumber=1"

    # Open the search query URL
    driver.get(search_query)

    # Wait for a few seconds to load the search results (you can adjust the waiting time)
    time.sleep(15)

    # You can now scrape or interact with the search results page as needed
    # For example, you can extract publication information here
    # Let's assume we extract publication links

    # Find all publication links on the page
    publication_links = driver.find_elements(By.CLASS_NAME, 'fw-bold')

    # Store the publication links in a list
    publication_links_list = [link.get_attribute("href") for link in publication_links]

    # Store faculty name and their publication links in the dictionary
    faculty_publications[faculty_name] = publication_links_list
    if len(publication_links_list) == 0:
        print(faculty_name)

    faculty_data = {
        "faculty": faculty_name,
        "university": university,
        "image": image,
        "website": website,
        "research_interests": research_interests,
        "publications": publication_links_list
    }

    # Append the faculty data to the list
    faculty_data_list.append(faculty_data)

    # To navigate back to the previous page for the next search
    driver.back()

# Close the browser window when done
driver.quit()

# Write the collected data to a JSON file
with open("faculty_publications.json", "w") as json_file:
    json.dump(faculty_data_list, json_file, indent=4)

# Print the collected data (for testing)
print(json.dumps(faculty_publications, indent=4))
