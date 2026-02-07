import db_creds
import requests
from requests.auth import HTTPBasicAuth


BASE = "http://127.0.0.1:5000/"

USERNAME = db_creds.USERNAME
PASSWORD = db_creds.PASSWORD
URLS = ['department', 'badges', 'job_titles', 'employees']

for x in URLS:
    response = requests.get(BASE + x)
    print('/'+x+', no credentials', response)

    response = requests.get(BASE + x, auth=HTTPBasicAuth(USERNAME, '0000'))
    print('/'+x+', incorrect credentials', response)

    response = requests.get(BASE + x, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    print('/'+x+', with credentials', response)
