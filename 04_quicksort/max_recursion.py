import unittest
import numpy as np


class TestMax(unittest.TestCase):

    def test_max(self):
        for i in range(100):
            arr = np.random.randint(-1000, 1000, size=30).tolist()
            max_arr = np.max(arr)

            self.assertEqual(max_recursion(arr), max_arr)


def max_recursion(arr: list, max_val=-np.inf):
    if arr:
        if arr[0] > max_val:
            max_val = arr[0]
        return max_recursion(arr[1:], max_val)
    return max_val


if __name__ == '__main__':
    unittest.main()
