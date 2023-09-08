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

# Initialize a Selenium webdriver (adjust the path to your WebDriver executable)
driver = webdriver.Chrome()

# Iterate through universities and faculties
for university_data in data:
    university = university_data["university"]
    faculties = university_data["faculties"]
    count = 0
    for faculty in faculties:
        faculty_name = faculty["name"]
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

            # Click the "Show More" button to load more publications (if any)
            while True:
                try:
                    show_more_button = driver.find_element(By.ID, "gsc_bpf_more")
                    # Check if the button is disabled
                    if show_more_button.is_enabled():
                        show_more_button.click()
                        time.sleep(5)
                    else:
                        break  # Exit the loop when the button is disabled
                except Exception:
                    break

            publications_id = driver.find_element(By.ID, "gsc_a_b")
            publications = publications_id.find_elements(By.TAG_NAME, "a")
            publications = [publication for publication in publications if "Cited by" not in publication.text]
            publications_links = [publication.get_attribute("href") for publication in publications]
            # Take the links that contain "citation_for_view" in their URL
            publications_links = [link for link in publications_links if "citation_for_view" in link]

            # Create a dictionary for each faculty
            faculty_info = {
                "university": university,
                "name": profile_name,
                "website": website_link,
                "research_interests": research_interests,
                "image": image,
                "publications": publications_links
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
with open("faculty_info.json", "w", encoding="utf-8") as json_file:
    json.dump(faculty_info_list, json_file, indent=4)
