import unittest
from multiphy_string import *


class Test(unittest.TestCase):
    def test_case(self):
        self.assertEqual(multiply('2', '3'), "6", "should be 6")
        self.assertEqual(multiply("123", "456"), "56088", "should be 56088")


if __name__ == "__main__":
    unittest.main()
