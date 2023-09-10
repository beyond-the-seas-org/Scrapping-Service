#After running this py file all the locations in "location_details.json" will be inserted into the database of "Analytic Service"

import json
import requests
locations =json.load(open("location_details_30_v2.json", encoding="utf8"))


try:
    response = requests.post('http://localhost:5003/api/analytics/add_locations',json= locations)
    print(response.json()['message'])


except Exception as e:
    print(e)
