import unittest
from strstr import *


class Test(unittest.TestCase):
    def test_case(self):
        self.assertEqual(strstr("hello", "ll"), 2, "should be 2")
        self.assertEqual(strstr("aaaaa", "bba"), -1, "should be -1")


if __name__ == "__main__":
    unittest.main()
