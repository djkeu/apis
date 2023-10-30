import unittest
from python_repos import api_call

class TestRepoMethods(unittest.TestCase):

    def test_api_call(self):
        self.assertEqual(api_call(), 200)
    
if __name__ == '__main__':
    unittest.main()
