import unittest
from utils.arrs import get
from utils.arrs import my_slice

import unittest

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1 + 1, 2)

    def test_get(self):
        self.assertEqual(get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(get([1, 2, 3], 10, "test"), "test")
        self.assertEqual(get([], 0, "test"), "test")

    def test_slice(self):
        self.assertEqual(my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(my_slice([1, 2, 3], 1), [2, 3])

    def test_slice_empty_array(self):
        self.assertEqual(my_slice([], 1, 3), [])

    def test_slice_start(self):
        self.assertEqual(my_slice([1, 2, 3], -10, 10), [1, 2, 3])
        self.assertEqual(my_slice([1, 2, 3], -2, 10), [2, 3])
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





def test_get(array, index, default, expected):
    assert get(array, index, default) == expected