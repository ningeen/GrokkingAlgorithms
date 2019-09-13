import unittest
import numpy as np


class TestSort(unittest.TestCase):

    def test_sort(self):
        for i in range(100):
            arr = np.sort(np.random.randint(-1000, 1000, size=100)).tolist()
            sorted_arr = np.sort(arr).tolist()

            self.assertEqual(selection_sort(arr), sorted_arr)


def find_smallest(arr):
    """
    Find smallest value in arr
    :param arr: list of numbers
    :return:    index of smallest number
    """
    smallest_idx = 0
    smallest = arr[smallest_idx]

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_idx = i

    return smallest_idx


def selection_sort(arr: list) -> list:
    """
    Selection sort instance
    :param arr:     list
    :return:        sorted list
    """

    sorted_arr = list()

    while len(arr) > 0:
        smallest_idx = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest_idx))

    return sorted_arr


if __name__ == '__main__':
    unittest.main()
