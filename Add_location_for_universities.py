#Author : Fahim

#After running this py file all the locations in "university.json" will be inserted into the database of "Analytic Service"

import json
import requests
universities =json.load(open("university.json", encoding="utf8"))


try:
    response = requests.post('http://localhost:5003/api/analytics/add_university_location',json= universities)

    print(response.json()['message'])


except Exception as e:
    print(e)



        
