import unittest
from palindome import *


class Test(unittest.TestCase):
    def test_case(self):
        self.assertEqual(palindome(121), True, "should be True")
        self.assertEqual(palindome(-121), False, "should be False")
        self.assertEqual(palindome(10), False, "should be False")


if __name__ == "__main__":
    unittest.main()
