from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Initialize a web driver (replace 'chromedriver' with the actual path to your driver)
driver = webdriver.Chrome()

# Open the desired URL
url = "https://csrankings.org/#/index?all&us"
driver.get(url)
time.sleep(20)

# Wait for the <select> element to be clickable
select_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "regions")))

# Find the option with the text "USA" and click on it
select = Select(select_element)
select.select_by_value("us")

# Wait for a moment to let the page update with the selected option
time.sleep(2)

inner_scroller = driver.find_element(By.CLASS_NAME, "table-responsive")

for j in range(0, 2):
    driver.execute_script(f"window.scrollTo(0,{(j+1)*100})")
    time.sleep(1)


# Scroll down the inner scroller
for j in range(0, 4):
    driver.execute_script(f"arguments[0].scrollTo(0, {(j+1)*50})", inner_scroller)
    print(f"Scrolling down... {j+1}")
    time.sleep(2)

# Find all <tr> elements with the specified class
table_rows = driver.find_elements(By.ID, "success")

#save this into a json file format
file = open("csrankings.json", "w", encoding="utf-8")

# Create a list to store the scraped data
data_list = []

# Iterate through the table rows
for row in table_rows:
    file.write(str(row.text) + "\n")
    file.flush()

# Close the browser window
driver.quit()
