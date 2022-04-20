import unittest
from two_sum import *


class Test(unittest.TestCase):
    def test_case(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1], "should be [0,1]")
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2], "should be [1,2]")
        self.assertEqual(two_sum([3, 3], 6), [0, 1], "should be [0,1]")


if __name__ == "__main__":
    unittest.main()
