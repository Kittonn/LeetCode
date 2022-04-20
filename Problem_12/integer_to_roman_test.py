import unittest
from integer_to_roman import *


class Test(unittest.TestCase):
    def test_case(self):
        self.assertEqual(intToroman(3), "III", "should be III")
        self.assertEqual(intToroman(58), "LVIII", "should be LVIII")
        self.assertEqual(intToroman(1994), "MCMXCIV", "should be MCMXCIV")


if __name__ == "__main__":
    unittest.main()
