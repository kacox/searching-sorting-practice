"""Implementations for Merge Sort."""

import unittest


## IMPLEMENTATION 1
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


## IMPLEMENTATION 2
def merge_sort_space_efficient(numbers, helper, low, high):
    """
    A more space efficient O(n) implementation of merge sort. Passes
    indices rather than slices (copies) to recursive and merge calls.
    
    Sorts items inplace with the assistance of a helper list.
    """
    # stop once inversion occurs (empty list)
    if low < high:
        mid = (low + high) // 2
        merge_sort_space_efficient(numbers, helper, low, mid)
        merge_sort_space_efficient(numbers, helper, mid + 1, high)
        merge_efficient(numbers, helper, low, mid, high)
    return numbers


def merge_efficient(numbers, helper, low, mid, high):
    """Merges sorted sublists into original array."""
    # copy both halves into a helper array
    for i in range(low, high + 1):
        helper[i] = numbers[i]

    # set additional helper variables (don't mod low, mid, high)
    left = low
    right = mid + 1
    current = low

    # iter thru helper array, copying back smaller element from left
    # and right sublists into original list (numbers)
    while (left <= mid) and (right <= high):
        # left element is smaller
        if helper[left] <= helper[right]:
            numbers[current] = helper[left]
            left += 1
        # right element is smaller
        else:
            numbers[current] = helper[right]
            right += 1
        # always increment current
        current += 1

    # copy the remaining left sublist into original list
    remaining = mid - left
    for index in range(remaining + 1):
        numbers[current + index] = helper[left + index]


## TESTS
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


class TestMSEfficient(unittest.TestCase):
    """Test merge_sort_space_efficient() functionality."""

    def test_null(self):
        numbers = []
        helper = []
        actual = merge_sort_space_efficient(numbers, helper, 0, 0)
        expected = []
        self.assertEqual(actual, expected)

    def test_single_repeated_number(self):
        numbers = [1, 1]
        helper = [None for num in numbers]
        actual = merge_sort_space_efficient(numbers, helper, 0, len(numbers) - 1)
        expected = [1, 1]
        self.assertEqual(actual, expected)

    def test_short_list(self):
        numbers = [1, 2, 3, 2]
        helper = [None for num in numbers]
        actual = merge_sort_space_efficient(numbers, helper, 0, len(numbers) - 1)
        expected = [1, 2, 2, 3]
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        numbers = [1, 2, 5, 5, 5, 5]
        helper = [None for num in numbers]
        actual = merge_sort_space_efficient(numbers, helper, 0, len(numbers) - 1)
        expected = [1, 2, 5, 5, 5, 5]
        self.assertEqual(actual, expected)

    def test_long_list(self):
        numbers = [4, 1, 4, 8, 3, 2, 7, 6, 5]
        helper = [None for num in numbers]
        actual = merge_sort_space_efficient(numbers, helper, 0, len(numbers) - 1)
        expected = [1, 2, 3, 4, 4, 5, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)