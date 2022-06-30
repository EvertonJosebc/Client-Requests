import json
import requests
from pprint import pprint

app_url = 'http://127.0.0.1:8090/countries/1'

todo = {"id":1 ,"name": "Thai", "capital": "Bankok", "area": '5131200'}

response = requests.put(app_url, json=todo)
pprint(response.json())
pprint(response.status_code)