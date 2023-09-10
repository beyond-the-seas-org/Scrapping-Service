import json
import requests

#After running this py file all the "fields" in "professors_details.json" will be inserted into the database of "Professor Service"

professors =json.load(open("professors_details.json", encoding="utf8"))



#finding all the fields(or area_of_interest)
all_fields = []
for professor in professors:
     for field in professor['research_interests']:
             all_fields.append(field.upper()) 

all_fields = list(set(all_fields))
print("Total fields: ",len(all_fields))

fields_json = {"fields":all_fields}

try:
    response = requests.post('http://localhost:5002/api/professors/add_fields',json= fields_json)
    print(response.json()['message'])


except Exception as e:
    print(e)