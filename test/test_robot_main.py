import unittest

from robot_main import *


class MyTestCase(unittest.TestCase):
    def test_input(self):
        self.assertEqual(placing, "PLACE")
        self.assertEqual(x_coordinate, 0 or 1 or 2 or 3 or 4, ValueError)
        self.assertEqual(y_coordinate,0 or 1 or 2 or 3 or 4, ValueError)
        self.assertEqual(z,'NORTH' or 'SOUTH' or 'EAST' or 'WEST', TypeError)


if __name__ == '__main__':
    unittest.main()
