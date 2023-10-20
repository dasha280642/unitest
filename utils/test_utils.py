import unittest
from utils.arrs import get
import unittest

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':
    unittest.main()

def test_get_existing_index():
    array = [1, 2, 3, 4, 5]
    index = 2
    assert get(array, index) == 3

def test_get_nonexistent_index():
    array = [1, 2, 3, 4, 5]
    index = 10
    default = None
    assert get(array, index, default) == default

def test_get_negative_index():
    array = [1, 2, 3, 4, 5]
    index = -1
    default = None
    assert get(array, index, default) == default

def test_get_empty_array():
    array = []
    index = 0
    default = "empty"
    assert get(array, index, default) == default

def test_get_default_value():
    array = [1, 2, 3, 4, 5]
    index = 10
    default = "not found"
    assert get(array, index, default) == default

def test_get_default_value_none():
    array = [1, 2, 3, 4, 5]
    index = 10
    default = None
    assert get(array, index, default) == default


def test_get(array, index, default, expected):
    assert get(array, index, default) == expected