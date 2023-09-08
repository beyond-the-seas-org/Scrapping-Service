from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# Read data from the JSON file
with open("university_professors.json", "r", encoding="utf-8") as data_file:
    data = json.load(data_file)

# Initialize a list to store faculty information
faculty_info_list = []
faculty_publications = {}
faculty_data_list = []

# Initialize a Selenium webdriver (adjust the path to your WebDriver executable)
driver = webdriver.Chrome()

# Iterate through universities and faculties
for university_data in data:
    university = university_data["university"]
    faculties = university_data["faculties"]
    count = 0
    for faculty in faculties:
        faculty_name = faculty["name"]
        # Open the IEEE Xplore website
        driver.get("https://ieeexplore.ieee.org/")

        # Build the search query URL for IEEE Xplore
        search_query = f"https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=({faculty_name})+AND+({university})&highlight=true&returnFacets=ALL&returnType=SEARCH&matchPubs=true&ranges=2010_2023_Year&pageNumber=1"

        # Open the search query URL
        driver.get(search_query)

        # Wait for a few seconds to load the search results (you can adjust the waiting time)
        time.sleep(10)

        # Find all publication links on the page
        publication_links = driver.find_elements(By.CLASS_NAME, 'fw-bold')

        # Store the publication links in a list
        publication_links_list = [link.get_attribute("href") for link in publication_links]

        if len(publication_links_list) == 0:
            print(faculty_name, " in " , university, ": No publications found", "\n")
            continue

        search_query = f"{faculty_name} {university} Google Scholar"

        # Open Google Search
        driver.get("https://www.google.com")

        # Find and fill the search input field
        search_input = driver.find_element(By.NAME, "q")
        search_input.send_keys(search_query)
        search_input.send_keys(Keys.RETURN)
        time.sleep(5)

        try:
            result_link = driver.find_element(By.CLASS_NAME, "yuRUbf")
            link = result_link.find_element(By.TAG_NAME, "a")
            link.click()
            time.sleep(5)
            profile_name_id = driver.find_element(By.ID, "gsc_prf_in")
            profile_name = profile_name_id.text
            print(profile_name)

            website_link_id = driver.find_element(By.ID, "gsc_prf_ivh")
            website_link = website_link_id.find_element(By.TAG_NAME, "a").get_attribute("href")
            print(website_link)

            research_interests_id = driver.find_element(By.ID, "gsc_prf_int")
            research_interests = research_interests_id.find_elements(By.TAG_NAME, "a")
            research_interests = [interest.text for interest in research_interests]
            print(research_interests)

            image_id = driver.find_element(By.ID, "gsc_prf_pu")
            image = image_id.find_element(By.TAG_NAME, "img").get_attribute("src")
            print(image)

            

            # Create a dictionary for each faculty
            faculty_info = {
                "university": university,
                "name": profile_name,
                "website": website_link,
                "research_interests": research_interests,
                "image": image,
                "publications": publication_links_list
            }

            # Add the faculty dictionary to the list
            faculty_info_list.append(faculty_info)
            count += 1
            if count == 10:
                break
        except Exception as e:
            print(f"Google Scholar profile not found for {faculty_name}")

# Close the browser window when done
driver.quit()

# Write the faculty information list to a JSON file
with open("professors_details.json", "w", encoding="utf-8") as json_file:
    json.dump(faculty_info_list, json_file, indent=4)
