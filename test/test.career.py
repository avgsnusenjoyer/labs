import unittest
import sys
import os
sys.path.append(os.path.abspath('../src'))
from career import solve_career

class TestCareer(unittest.TestCase):
    def test_example_1(self):
        L = 4
        pyramid = [
            [4],
            [3, 1],
            [2, 1, 5],
            [1, 3, 2, 1]
        ]
        self.assertEqual(solve_career(L, pyramid), 12)

    def test_example_2(self):
        L = 1
        pyramid = [
            [9999]
        ]
        self.assertEqual(solve_career(L, pyramid), 9999)

    def test_example_3(self):
        L = 5
        pyramid = [
            [0],
            [1, 1],
            [0, 0, 0],
            [1, 1, 1, 1],
            [0, 1, 0, 1, 0]
        ]
        self.assertEqual(solve_career(L, pyramid), 3)

if __name__ == '__main__':
    unittest.main()
