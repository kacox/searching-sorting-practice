"""Implementation of the Quick Sort algorithm.

Average case: O(n log n)
Worst (rarer) case: O(n**2)
"""

import unittest


def quick_sort(num_list, left_indx, right_indx):
    # get pivot (middle value)
    pivot = num_list[(left_indx + (right_indx - left_indx) // 2)]
    i = left_indx
    j = right_indx

    # loop until inversion
    while i <= j:
        # left progression
        while pivot > num_list[i]:
            i += 1

        # right progression
        while pivot < num_list[j]:
            j -= 1

        # if no inversion
        if i <= j:
            # swap left and right VALUES
            num_list[i], num_list[j] = num_list[j], num_list[i]

            # adjust left and right indices
            i += 1
            j -= 1

    if left_indx < j:
        quick_sort(num_list, left_indx, j)
    if i < right_indx:
        quick_sort(num_list, i, right_indx)

    return num_list


class Test(unittest.TestCase):

    def test_single_repeated_number(self):
        actual = quick_sort([1, 1], 0, 1)
        expected = [1, 1]
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = quick_sort([1, 2, 3, 2], 0, 3)
        expected = [1, 2, 2, 3]
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = quick_sort([1, 2, 5, 5, 5, 5], 0, 5)
        expected = [1, 2, 5, 5, 5, 5]
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = quick_sort([4, 1, 4, 8, 3, 2, 7, 6, 5], 0, 8)
        expected = [1, 2, 3, 4, 4, 5, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)