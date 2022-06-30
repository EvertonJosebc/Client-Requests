import json
import requests
from pprint import pprint

app_url = 'http://127.0.0.1:8090/countries'
response = requests.get(app_url)
pprint(response.json())

insert = {
    1: {"name": "Brasil", "capital": "Brasilia", "area": 783120},
    2: {"name": "Austria", "capital": "berra", "area": 617930},
    3: {"name": "Et", "capital": "Lunaticos", "area": 1610408},
}

for i_id in insert:
    response = requests.post(app_url, json=insert[i_id])
 
pprint(response.json())
pprint(response.status_code)