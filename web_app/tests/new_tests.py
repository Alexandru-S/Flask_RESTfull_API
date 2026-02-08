import unittest
import requests
import db_creds
from requests.auth import HTTPBasicAuth

BASE = "http://127.0.0.1:5000/"

USERNAME = db_creds.USERNAME
PASSWORD = db_creds.PASSWORD
URLS = ['department', 'badges', 'job_titles', 'employees']


class LogInTest(unittest.TestCase):
    """Tests authentication outcomes for protected API endpoints."""
    def test_login(self):
        """Verifies correct for all endpoints."""
        for x in URLS:
            response = requests.get(
                BASE + x, 
                auth=HTTPBasicAuth(USERNAME, 
                PASSWORD))
            print('URL>>>>>>>>>', x)
            self.assertEqual(200, response.status_code)
            self.assertEqual(int, type(response.status_code))

    def test_wrong_login(self):
        """Verifies wrong requests return 401 for all endpoints."""
        auth = HTTPBasicAuth(USERNAME, '0000')
        for x in URLS:
            response = requests.get(BASE + x, auth=auth)
            print('URL>>>>>>>>>', x)
            self.assertEqual(401, response.status_code)
            self.assertEqual(int, type(response.status_code))

    def test_no_login(self):
        """Verifies unauthenticated requests return 401 for all endpoints."""
        for x in URLS:
            response = requests.get(BASE + x)
            print('URL>>>>>>>>>', x)
            self.assertEqual(401, response.status_code)
            self.assertEqual(int, type(response.status_code))


if __name__ == '__main__':
    unittest.main()
