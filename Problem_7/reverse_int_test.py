import unittest
from reverse_int import *


class Test(unittest.TestCase):
    def test_case(self):
        self.assertEqual(reverse_int(123), 321, "should be 321")
        self.assertEqual(reverse_int(-123), -321, "should be -321")
        self.assertEqual(reverse_int(120), 21, "should be 21")
        self.assertEqual(reverse_int(1534236469), 0, "should be 0")


if __name__ == "__main__":
    unittest.main()
