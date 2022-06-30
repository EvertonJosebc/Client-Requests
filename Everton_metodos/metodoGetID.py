import json
import requests
from pprint import pprint

app_url = 'http://127.0.0.1:8090/countries/1'
response = requests.get(app_url)

pprint(response.json())
pprint(response.status_code)