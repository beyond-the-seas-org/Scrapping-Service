from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_university_location_with_selenium(university_name):
    driver = webdriver.Chrome()

    try:
        # Construct the Google search URL
        search_url = f"https://www.google.com/search?q={university_name}"

        # Open the URL in the browser
        driver.get(search_url)
        time.sleep(2)
        
        desired_url_pattern = "https://en.wikipedia.org/"
        link_element = driver.find_element(By.PARTIAL_LINK_TEXT, "Wikipedia")  # Click on the Wikipedia link
        link_element.click()
        time.sleep(2)

        # Extract location information
        locality = driver.find_element(By.CLASS_NAME, 'locality')
        state = driver.find_element(By.CLASS_NAME, 'state')
        # country = driver.find_element(By.CLASS_NAME, 'country-name')
        country = "United States"

        location = f"{locality.text}, {state.text}, {country}"
        return location

    except Exception as e:
        return "Location not found"

    finally:
        driver.quit()


#read the file filtered_data.json and store it in a variable
import json
with open("filtered_data.json", "r") as file:
    data = json.load(file)


location_file = open("location.json", "w")
#loop through the data and take the name as university_name
location_file.write("[\n")
for item in data:
    university_name = item["name"]
    rank = item["rank"]
    location = get_university_location_with_selenium(university_name)
    location_data = {
        "name": university_name,
        "rank": rank,
        "location": location
    }
    json_data = json.dumps(location_data, indent=4)
    location_file.write(json_data)
    location_file.write(",\n")
    location_file.flush()

location_file.write("]")