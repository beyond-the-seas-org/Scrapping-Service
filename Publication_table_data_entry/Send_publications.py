#After running this py file all the publications in "professors_ieee_publications.json" will be inserted into the database of "Analytic Service"

import json
import requests
locations =json.load(open("professors_ieee_publications.json", encoding="utf8"))


try:
    response = requests.post('http://localhost:5002/api/professors/add_all_publications',json= locations)
    print(response.json()['message'])


except Exception as e:  
    print(e)
