import unittest
import requests

class TestGitHubAPI(unittest.TestCase):
    def test_api_status_code(self):
        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        headers = {'Accept': 'application/vnd.github.v3+json'}
        r = requests.get(url, headers=headers)

        # Check if the status code is 200 (OK)
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()
