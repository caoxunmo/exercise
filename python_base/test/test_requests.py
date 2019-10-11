import unittest
from python_base.demo_requests import getData

class MyTestCase(unittest.TestCase):
    def test_something(self):
        url = 'https://www.baidu.com/'
        result = getData(url)


if __name__ == '__main__':
    unittest.main()
