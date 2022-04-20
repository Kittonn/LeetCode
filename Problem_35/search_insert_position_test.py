import unittest
from search_insert_position import *


class Test(unittest.TestCase):
    def test_case(self):
        self.assertEqual(searchInsert([1, 3, 5, 6],5), 2, "should be 2")
        self.assertEqual(searchInsert([1, 3, 5, 6],2), 1, "should be 1")
        self.assertEqual(searchInsert([1, 3, 5, 6],7), 4, "should be 4")


if __name__ == "__main__":
    unittest.main()
