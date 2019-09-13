import unittest
import numpy as np


class TestSort(unittest.TestCase):

    def test_sort(self):
        # 7s 336ms
        for i in range(10000):
            arr = np.sort(np.random.randint(-1000, 1000, size=100)).tolist()
            sorted_arr = np.sort(arr).tolist()

            self.assertEqual(quick_sort(arr), sorted_arr)

    def test_sort_rand(self):
        # 3s 335ms
        for i in range(10000):
            arr = np.sort(np.random.randint(-1000, 1000, size=100)).tolist()
            sorted_arr = np.sort(arr).tolist()

            self.assertEqual(quick_sort_rand(arr), sorted_arr)


def quick_sort(arr):
    """
    Quick sort
    :param arr: list
    :return:    sorted list
    """
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    less = [val for val in arr[1:] if val < pivot]
    greater = [val for val in arr[1:] if val >= pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


def quick_sort_rand(arr):
    """
    Quick sort
    :param arr: list
    :return:    sorted list
    """
    if len(arr) < 2:
        return arr

    pivot_idx = np.random.randint(len(arr))
    pivot = arr[pivot_idx]
    less = [val for i, val in enumerate(arr) if val < pivot and i != pivot_idx]
    greater = [val for i, val in enumerate(arr) if val >= pivot and i != pivot_idx]
    return quick_sort_rand(less) + [pivot] + quick_sort_rand(greater)


if __name__ == '__main__':
    unittest.main()
