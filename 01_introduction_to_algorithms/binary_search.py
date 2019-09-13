import unittest


class TestSearch(unittest.TestCase):
    arr = [0, 1, 11, 22, 34, 56]
    arr_two = list(range(-1000, 1000, 17))

    def test_if_exists(self):
        for arr in [self.arr, self.arr_two]:
            for i, val in enumerate(arr):
                self.assertEqual(binary_search(arr, val), i)

    def test_if_none(self):
        values_not_in_arr = [-5, 5, 100, -70]
        for val in values_not_in_arr:
            self.assertIsNone(binary_search(self.arr, val))


def binary_search(arr, val):
    """
    Binary search
    :param arr: sorted array
    :param val: value to find
    :return:    index of val in arr
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == val:
            return mid

        if guess < val:
            low = mid + 1
        else:
            high = mid - 1

    return None


if __name__ == '__main__':
    unittest.main()
