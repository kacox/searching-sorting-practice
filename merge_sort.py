"""Implementation for Merge Sort."""

import unittest


def merge_sort_space_expensive(numbers):
    """Merge sort implemented by passing slices to recursive calls."""
    # Base case
    if len(numbers) <= 1:
        return numbers

    # Recursive case
    mid_pt = len(numbers) // 2
    left = merge_sort_space_expensive(numbers[:mid_pt])
    right = merge_sort_space_expensive(numbers[mid_pt:])

    # Merging phase
    return merge_se(left, right)


def merge_se(left, right):
    """Returns a single sorted, merged list."""
    sorted_list = []
    while len(left) or len(right):
        if len(left) and len(right):
            # while they both have elements
            if left[0] > right[0]:
                # choose right element
                sorted_list.append(right.pop(0))
            else:
                # choose left element
                sorted_list.append(left.pop(0))
        elif not len(left):
            # must choose right
            sorted_list.append(right.pop(0))
        else:
            # must choose left
            sorted_list.append(left.pop(0))

    return sorted_list


class TestMSSpaceExpensive(unittest.TestCase):
    """Test merge_sort_space_expensive() functionality."""

    def test_null(self):
        actual = merge_sort_space_expensive([])
        expected = []
        self.assertEqual(actual, expected)

    def test_single_repeated_number(self):
        actual = merge_sort_space_expensive([1, 1])
        expected = [1, 1]
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = merge_sort_space_expensive([1, 2, 3, 2])
        expected = [1, 2, 2, 3]
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = merge_sort_space_expensive([1, 2, 5, 5, 5, 5])
        expected = [1, 2, 5, 5, 5, 5]
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = merge_sort_space_expensive([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = [1, 2, 3, 4, 4, 5, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)