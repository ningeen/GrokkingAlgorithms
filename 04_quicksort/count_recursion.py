import unittest
import numpy as np


class TestCount(unittest.TestCase):

    def test_count(self):
        for i in range(100):
            arr = np.zeros(np.random.randint(500)).tolist()
            count = len(arr)

            self.assertEqual(count_recursion(arr), count)


def count_recursion(arr: list):
    if arr:
        return 1 + count_recursion(arr[1:])
    return 0


if __name__ == '__main__':
    unittest.main()
