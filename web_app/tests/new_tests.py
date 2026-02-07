import unittest
import requests
import db_creds
from requests.auth import HTTPBasicAuth

BASE = "http://127.0.0.1:5000/"

USERNAME = db_creds.USERNAME
PASSWORD = db_creds.PASSWORD
URLS = ['department', 'badges', 'job_titles', 'employees']


class LogInTest(unittest.TestCase):
    def test_login(self):
        for x in URLS:
            response = requests.get(BASE + x, auth=HTTPBasicAuth(USERNAME, PASSWORD))
            print('URL>>>>>>>>>', x)
            self.assertEqual(200, response.status_code)
            self.assertEqual(int, type(response.status_code))

    def test_wrong_login(self):
        auth = HTTPBasicAuth(USERNAME, '0000')
        for x in URLS:
            response = requests.get(BASE + x, auth=auth)
            print('URL>>>>>>>>>', x)
            self.assertEqual(401, response.status_code)
            self.assertEqual(int, type(response.status_code))

    def test_no_login(self):
        for x in URLS:
            response = requests.get(BASE + x)
            print('URL>>>>>>>>>', x)
            self.assertEqual(401, response.status_code)
            self.assertEqual(int, type(response.status_code))


if __name__ == '__main__':
    unittest.main()
