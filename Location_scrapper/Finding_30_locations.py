#After running this py file all the locations in "location_details.json" will be inserted into the database of "Analytic Service"

import json
import requests
from location_details_scrapper_30 import *
university_json =json.load(open("university_professors.json", encoding="utf8"))

#finding the list of locations
universities = []
for university in university_json:
    universities.append(university['university'])

print("Total universities: ",len(universities))
#finding the list of locations for above universites
location_json =json.load(open("university.json", encoding="utf8"))

locations = []
for location in location_json:
    if location['name'] in universities and location['location'] != "Location not found":
        locations.append(location['location'])

print("Total locations: ",len(locations))

# for location in locations:
#     print(location)

_30_location_file = open("location_details_30_v2.json", "w")
_30_location_file.write("[\n")

total_location_details_extracted=0

# locations = ['Westwood, Los Angeles, California, United States','Amherst, Massachusetts, United States','New Brunswick, Piscataway, New Jersey, United States']

for location in locations:
     
    location_data = get_location_details_with_selenium(location)

    #if any error occured while scrapping the location data then continue
    if(location_data.keys().__contains__("error")):
        continue
    
    if(total_location_details_extracted > 0):
        _30_location_file.write(",\n")
    
    json_data = json.dumps(location_data, indent=4)
    _30_location_file.write(json_data)
    _30_location_file.flush()
    total_location_details_extracted += 1
    print("location: ", location," extracted successfully")
    print("total_location_details_extracted: ", total_location_details_extracted)

_30_location_file.write("\n]")


#Now finding the details of this 30 location from "location_details_2.json"
# location_details_json =json.load(open("location_details_2.json", encoding="utf8"))

# _30_location_file = open("location_details_30.json", "w")
# _30_location_file.write("[\n")

# for location_dict in location_details_json:
#     for location in locations:
#        # print(location)
#         location_name_state_country = location.split(", ") 
#         #print(location_name_state_country)

#         location_name = location_name_state_country[0]
#         state_name = location_name_state_country[1]
#         country_name = location_name_state_country[len(location_name_state_country)-1]

#         if(location_dict['location_name'] == location_name and location_dict['state'] == state_name and location_dict['country'] == country_name):
#             _30_location_file.write(json.dumps(location_dict, indent=4))
#             _30_location_file.write(",\n")
#             locations.remove(location)
#             break

# _30_location_file.write("\n]")
        


   
# try:
#     response = requests.post('http://localhost:5003/api/analytics/add_locations',json= locations)
#     print(response.json()['message'])


# except Exception as e:
#     print(e)
