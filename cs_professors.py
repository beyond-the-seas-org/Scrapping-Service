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

# # Wait for the <select> element to be clickable
select_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "regions")))

# # Find the option with the text "USA" and click on it
select = Select(select_element)
select.select_by_value("us")

# # Wait for a moment to let the page update with the selected option
time.sleep(2)

# inner_scroller = driver.find_element(By.CLASS_NAME, "table-responsive")

# for j in range(0, 2):
#     driver.execute_script(f"window.scrollTo(0,{(j+1)*100})")
#     time.sleep(1)


# I have a dataset in university.json file as following:
# [{
#     "name": "Carnegie Mellon University",
#     "rank": "1",
#     "location": "Pittsburgh, Pennsylvania, United States"
# },
# {
#     "name": "Univ. of Illinois at Urbana-Champaign",
#     "rank": "2",
#     "location": "Urbana and Champaign, Illinois, United States"
# },]
# I want to read the name and split it in respect to space. then replace %20 for space and make id
# for example id = Carnegie%20Mellon%20University-widget

universities = open("university.json", "r", encoding="utf-8")
universities = universities.read()
universities = eval(universities)

file = open(f"professors.json", "w", encoding="utf-8")

try:
    for university in universities:
        university_name = university["name"]
        name = university_name.split(" ")
        name = "%20".join(name)
        id = name + "-widget"
        # click on this id
        driver.find_element(By.ID, id).click()
        time.sleep(2)

except Exception as e:
    print(e)
    pass

# Find all <tr> elements with the specified class
table_rows = driver.find_elements(By.ID, "success")
# save this into a json file format
# Create a list to store the scraped data
data_list = []
# Iterate through the table rows
for row in table_rows:
    #take the first column and write it into a file
    first_col = row.find_element(By.TAG_NAME, "td")
    first_col = first_col.text
    file.write(str(first_col) + "\n")
    file.flush()


file.close()

# Close the browser window
driver.quit()
