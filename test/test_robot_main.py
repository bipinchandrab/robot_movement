import unittest

from robot_main import *


class MyTestCase(unittest.TestCase):
    def test_input(self):
        self.assertEqual(placing, "PLACE")
        assert True


if __name__ == '__main__':
    unittest.main()
