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


def binary_search(arr, val, idx=0):
    """
    Recursive binary search
    :param arr: sorted array
    :param val: value to find
    :param idx: index of first element in arr for original array
    :return:    index of val in arr or halved arr
    """

    if len(arr) == 1:
        if arr[0] == val:
            return idx
        return None

    mid = len(arr) // 2
    guess = arr[mid]

    if guess > val:
        return binary_search(arr[:mid], val, idx)
    else:
        return binary_search(arr[mid:], val, idx + mid)


if __name__ == '__main__':
    unittest.main()
