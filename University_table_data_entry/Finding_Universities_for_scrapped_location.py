#After running this py file all the locations in "location_details.json" will be inserted into the database of "Analytic Service"

import json
import requests
university_json =json.load(open("university.json", encoding="utf8"))
location_json =json.load(open("location_details_30_v2.json", encoding="utf8"))

_30_university_file = open("university_30.json", "w")
_30_university_file.write("[\n")


total_unversity_count = 0

for university in university_json:
    if(university['location'] == "Location not found"):
        continue
    university_location_state_country = university['location'].split(", ")
    location_name = university_location_state_country[0]
    state_name = university_location_state_country[1]
    country_name = university_location_state_country[len(university_location_state_country)-1]

    for location in location_json:
        if(location['location_name'] == location_name and location['state'] == state_name and location['country'] == country_name):
            if(total_unversity_count > 0):
               _30_university_file.write(",\n")
    
            json_data = json.dumps(university, indent=4)
            _30_university_file.write(json_data)
            _30_university_file.flush()
            total_unversity_count += 1
            break

_30_university_file.write("\n]")

print(total_unversity_count)




