#After running this py file all the "professors,professor_publication,professor_area_of_interest" entries  will be inserted into the database of "Professor Service"

import json
import requests
professors =json.load(open("professors_details.json", encoding="utf8"))

try:
    response = requests.post('http://localhost:5002/api/professors/add_professors_complete_info',json= professors)
    print(response.json()['message'])


except Exception as e:
    print(e)
