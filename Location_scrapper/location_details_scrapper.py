from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

def get_location_details_with_selenium(location):

    chrome_options = Options()
    # disabling the pop up of browser window
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Construct the Google search URL
        searched_term = f"{location} bestplace.net"
        search_url = f"https://www.google.com/search?q={searched_term}"

        # Open the URL in the browser
        driver.get(search_url)
        time.sleep(2)
        
        #desired_url_pattern = "https://en.wikipedia.org/"
        link_element = driver.find_element(By.PARTIAL_LINK_TEXT, "https://www.bestplaces.net")  # Click on the Wikipedia link
        link_element.click()
        time.sleep(5)

        location_data = {}

        location_name_state_country = location.split(", ")
        location_data['location_name'] = location_name_state_country[0]
        location_data['state'] = location_name_state_country[1]
        location_data['country'] = location_name_state_country[len(location_name_state_country) - 1]


        #exytracting location short details
        try:
            shortdetails = driver.find_elements(By.CLASS_NAME, 'card-body')

            rows = shortdetails[0].find_elements(By.CLASS_NAME, 'row')

            columns = rows[0].find_elements(By.CLASS_NAME, 'col-md-4')

            population_and_unemployment = columns[0].find_elements(By.TAG_NAME, 'p')
           # print(population)

            # print("Population: ", population_and_unemployment[1].text)
            # print("Unemployment rate: ", population_and_unemployment[4].text)
            location_data['population'] = population_and_unemployment[1].text
            location_data['unemployment_rate'] = population_and_unemployment[4].text

            cost_of_living_and_home_price = columns[1].find_elements(By.TAG_NAME, 'p')
            # print("Cost of living: ", cost_of_living_and_home_price[1].text)
            # print("Home price: ", cost_of_living_and_home_price[3].text)
            location_data['cost_of_living'] = cost_of_living_and_home_price[1].text
            location_data['home_price'] = cost_of_living_and_home_price[3].text


            median_income_and_weather_comfort_index = columns[2].find_elements(By.TAG_NAME, 'p')
            # print("Median income: ", median_income_and_weather_comfort_index[1].text)
            # print("Weather comfort index: ", median_income_and_weather_comfort_index[3].text)
            location_data['median_income'] = median_income_and_weather_comfort_index[1].text
            location_data['weather_comfort_index'] = median_income_and_weather_comfort_index[3].text


       

        except Exception as e:
            print("Exception in short details scrapper")
            short_details_exception_file.write(location+"\n")
            short_details_exception_file.flush()
            print(e)
            return {"error":"Error in location details scrapping"}




        #extracting location full details
        try:

            full_details = driver.find_elements(By.CLASS_NAME, 'col-xl-7')
            rows = full_details[0].find_elements(By.CLASS_NAME, 'row')
            columns = rows[6].find_elements(By.CLASS_NAME, 'col-md-12')
         
            lines = columns[0].text.split("\n")
            detailed_info = {}
            for i in range(0, len(lines), 2):                
                details = lines[i+1].split(". ")
                details = details[0:(len(details)-1)]
                details = ". ".join(details)
                detailed_info[lines[i]] = details

            #print(dict)

        except Exception as e:
            print("Exception in full details scrapper")
            full_details_exception_file.write(location+"\n")
            full_details_exception_file.flush()
            print(e)
            return {"error":"Error in location details scrapping"}



        #extracting image_link of that location
        try:
            # searched_term = f"{location} gettyimages.com"
            # search_url = f"https://www.google.com/search?q={searched_term}"

            # # Open the URL in the browser
            # driver.get(search_url)
            # time.sleep(2)
            
            # #desired_url_pattern = "https://en.wikipedia.org/"
            # link_element = driver.find_element(By.PARTIAL_LINK_TEXT, "https://www.gettyimages.com")  # Click on this link
            # link_element.click()
            # time.sleep(5)


            # image = driver.find_elements(By.CLASS_NAME, 'BLA_wBUJrga_SkfJ8won')
            # image_link= image[0].get_attribute('src')


            image = driver.find_elements(By.CLASS_NAME, 'bt-0')
            image_style = image[0].get_attribute('style')

            image_url = image_style.split(" ")[1]
            image_link = image_url[5:len(image_url)-2]

        except Exception as e:
            print("Exception in image_link scrapper")
            image_link_exception_file.write(location+"\n")
            image_link_exception_file.flush()
            print(e)
            return {"error":"Error in image link scrapping"}


        location_data['image_link'] = image_link 

        location_data['detailed_info'] = detailed_info 



        return location_data  

                

    except Exception as e:
        Location_details_not_found_file.write(location+"\n")
        Location_details_not_found_file.flush()
        return {"error":"Location details not found"}

    finally:
        driver.quit()


import json
with open("university.json", "r") as file:
    data = json.load(file)


location_file = open("location_details_2.json", "w")
total_location_details_extracted = 0
#loop through the data and take the name as university_name
location_file.write("[\n")

short_details_exception_file = open("short_details_exception_2.txt", "w")
full_details_exception_file = open("full_details_exception_2.txt", "w")
image_link_exception_file = open("image_link_exception.txt_2", "w")
Location_details_not_found_file = open("Location_details_not_found_2.txt", "w")

for item in data:
    
    location = item.get("location")

    if(location == "Location not found"):
        continue

    location_data = get_location_details_with_selenium(location)

    #if any error occured while scrapping the location data then continue
    if(location_data.keys().__contains__("error")):
        continue
    
    if(total_location_details_extracted > 0):
        location_file.write(",\n")
    
    json_data = json.dumps(location_data, indent=4)
    location_file.write(json_data)
    location_file.flush()
    total_location_details_extracted += 1
    print("location: ", location," extracted successfully")
    print("total_location_details_extracted: ", total_location_details_extracted)

location_file.write("\n]")

#get_location_details_with_selenium("Pittsburgh, Pennsylvania, United States")