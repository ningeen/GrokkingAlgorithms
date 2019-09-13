import unittest
import numpy as np


class TestSum(unittest.TestCase):

    def test_sum(self):
        for i in range(100):
            arr = np.random.randint(-1000, 1000, size=100).tolist()
            sum_arr = np.sum(arr)

            self.assertEqual(sum_recursion(arr), sum_arr)


def sum_recursion(arr: list):
    if arr:
        return arr[0] + sum_recursion(arr[1:])
    return 0


if __name__ == '__main__':
    unittest.main()
