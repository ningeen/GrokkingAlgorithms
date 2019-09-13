import unittest


class TestSearch(unittest.TestCase):
    arr = [0, 1, 11, 15, 22, 34, 56]
    arr_two = list(range(-1000, 1000, 17))

    def test_if_exists(self):
        for arr in [self.arr, self.arr_two]:
            for i, val in enumerate(arr):
                self.assertEqual(binary_search(arr, val), i)

    def test_if_none(self):
        values_not_in_arr = [-5, 5, 100, -70]
        for val in values_not_in_arr:
            self.assertIsNone(binary_search(self.arr, val))


def binary_search(arr, val, low=0):
    """
    Recursive binary search
    :param arr: sorted array
    :param val: value to find
    :param low: original index of first value in array
    :return:    index of val in arr
    """

    mid = len(arr) // 2
    guess = arr[mid]

    try:
        if guess == val:
            return low + mid
        elif guess > val:
            return binary_search(arr[:mid], val, low)
        else:
            return binary_search(arr[mid + 1:], val, low + mid + 1)
    except IndexError:
        return None


if __name__ == '__main__':
    unittest.main()
