import unittest
from utils.arrs import get

class TestUtils(unittest.TestCase):
    def test_some_function(self):
        result = get([2, 3], 1)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()