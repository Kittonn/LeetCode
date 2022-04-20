import unittest
from pow import *


class Test(unittest.TestCase):
    def test_case(self):
        self.assertEqual(myPow(2.00000, 10), 1024.00000,
                         "should be 1024.00000")
        self.assertEqual(myPow(2.10000, 3), 9.26100, "should be 9.26100")
        self.assertEqual(myPow(2.00000, -2), 0.25000, "should be 0.25000")


if __name__ == "__main__":
    unittest.main()
