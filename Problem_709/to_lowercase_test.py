import unittest
from to_lowercase import *


class Test(unittest.TestCase):
    def test_case(self):
        self.assertEqual(toLowerCase("Hello"), 'hello', "should be 'hello'")
        self.assertEqual(toLowerCase("here"), 'here', "should be 'here'")
        self.assertEqual(toLowerCase('LOVELY'), 'lovely', "should be 'lovely'")


if __name__ == "__main__":
    unittest.main()
