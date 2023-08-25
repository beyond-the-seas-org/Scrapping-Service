from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select


# Initialize a web driver (replace 'chromedriver' with the actual path to your driver)
driver = webdriver.Chrome()

# Open the desired URL
url = "https://csrankings.org/#/index?all&us"
driver.get(url)
time.sleep(10)

# Wait for the <select> element to be clickable
select_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "regions")))

# Find the option with the text "USA" and click on it
select = Select(select_element)
select.select_by_value("us")

# Wait for a moment to let the page update with the selected option
time.sleep(2)

# Locate the element by ID and click on it to expand the list
element = driver.find_element(By.ID, "Carnegie%20Mellon%20University-widget")
element.click()

# Wait for the list of faculties to load (adjust the timeout as needed)
time.sleep(5)
file = open("faculty.json", "w", encoding="utf-8")

elements = driver.find_elements(By.CLASS_NAME, "table")
for element in elements:
    faculty_elements = element.find_elements(By.TAG_NAME, "a")
    for faculty_element in faculty_elements:
        professor_name = faculty_element.text
        if professor_name != "" and professor_name != "on" and professor_name != "off":
            #if it is a numeric value, it is not a professor name
            if not professor_name.isnumeric():
                file.write(professor_name + "\n")
                file.flush()

file.close()

# Close the browser window
driver.quit()
