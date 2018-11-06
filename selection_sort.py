"""
Implementation for Selection Sort.

O(n**2) runtime.
"""

import unittest


def selection_sort(numbers):
    if numbers:

        for idx in range(len(numbers) - 1):
            smallest_so_far = numbers[idx]
            sm_idx = idx

            for subsequent in range(idx + 1, len(numbers)):
                if numbers[subsequent] < smallest_so_far:
                    smallest_so_far = numbers[subsequent]
                    sm_idx = subsequent

            # save yourself a swap if already sorted
            if smallest_so_far is not numbers[idx]:
                numbers[idx], numbers[sm_idx] = numbers[sm_idx], numbers[idx]

    return numbers


class TestSort(unittest.TestCase):
    """Test selection_sort() functionality."""

    def test_null(self):
        actual = selection_sort([])
        expected = []
        self.assertEqual(actual, expected)

    def test_single_repeated_number(self):
        actual = selection_sort([1, 1])
        expected = [1, 1]
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = selection_sort([1, 2, 3, 2])
        expected = [1, 2, 2, 3]
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = selection_sort([1, 2, 5, 5, 5, 5])
        expected = [1, 2, 5, 5, 5, 5]
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = selection_sort([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = [1, 2, 3, 4, 4, 5, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)