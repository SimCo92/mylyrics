import mylyrics
import pytest
import unittest

def test():
    pass

class integrationTest():

    def test_get_request():
        response = requests.get('http://google.it')
        assert response.status_code == 200



class unittTest(unittest.TestCase):

    def test(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

