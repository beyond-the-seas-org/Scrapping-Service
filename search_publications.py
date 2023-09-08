from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize a Selenium webdriver (adjust the path to your WebDriver executable)
driver = webdriver.Chrome()

# Sample data
data = {
    "university": "University of Wisconsin - Madison",
    "faculties": [
        {"name": "Ilias Diakonikolas"},
        {"name": "Vikas Singh"},
        {"name": "Somesh Jha"},
        {"name": "Loris D'Antoni"},
        {"name": "Yong Jae Lee"},
        {"name": "Bilge Mutlu"}
    ]
}

# Open the IEEE Xplore website
driver.get("https://ieeexplore.ieee.org/")

# Iterate through faculty names and search for their publications
for faculty in data["faculties"]:
    faculty_name = faculty["name"]
    university = data["university"]

    # Build the search query URL for IEEE Xplore
    search_query = f"https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=({faculty_name})+AND+({university})&highlight=true&returnFacets=ALL&returnType=SEARCH&matchPubs=true&ranges=2019_2023_Year&pageNumber=1"

    # Open the search query URL
    driver.get(search_query)

    # Wait for a few seconds to load the search results (you can adjust the waiting time)
    time.sleep(15)

    # You can now scrape or interact with the search results page as needed
    # For example, you can extract publication information here

    # To navigate back to the previous page for the next search
    driver.back()

# Close the browser window when done
driver.quit()
