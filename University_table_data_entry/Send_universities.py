#After running this py file all the universities in "university_30.json" will be inserted into the database of "Professor Service"

import json
import requests
locations =json.load(open("university_30.json", encoding="utf8"))


#print(len(locations))
try:
    response = requests.post('http://localhost:5002/api/professors/add_university_rank',json= locations)
    print(response.json()['message'])


except Exception as e:
    print(e)
