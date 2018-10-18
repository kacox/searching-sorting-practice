"""
Implementation of Insertion Sort.

'Sorting is typically done in-place, by iterating up the array, growing
the sorted list behind it. At each array-position, it checks the value there
against the largest value in the sorted list (which happens to be next to it,
in the previous array-position checked). If larger, it leaves the element in
place and moves to the next. If smaller, it finds the correct position
within the sorted list, shifts all the larger values up to make a space, and
inserts into that correct position.'
"""

import unittest


def insertion_sort(numbers):
    # skip the first index, can't swap it anyway
    i = 1
    while i < len(numbers):
        j = i
        # keep swapping until its proper place found
        while j > 0 and numbers[j - 1] > numbers[j]:
            # swap
            numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]
            # progress backwards
            j -= 1
        # do this for the next element in the array
        i += 1

    return numbers


class Test(unittest.TestCase):

    def test_null(self):
        actual = insertion_sort([])
        expected = []
        self.assertEqual(actual, expected)

    def test_simple_repeat(self):
        actual = insertion_sort([1, 1])
        expected = [1, 1]
        self.assertEqual(actual, expected)

    def test_medium_repeat(self):
        actual = insertion_sort([2, 1, 1, 3])
        expected = [1, 1, 2, 3]
        self.assertEqual(actual, expected)

    def test_small(self):
        actual = insertion_sort([2, 1])
        expected = [1, 2]
        self.assertEqual(actual, expected)

    def test_medium(self):
        actual = insertion_sort([4, 12, 1, 3, 2])
        expected = [1, 2, 3, 4, 12]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)