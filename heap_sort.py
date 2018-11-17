"""
Implementation for heap sort using Python's heapq.
See: https://www.youtube.com/watch?v=2DmK_H7IdTo

1. Create heap (min or max depending on what you want)
2. Remove minimum (min heap) or maximum (max heap) item
3. Place item in sorted partition (at the end of the list)
    - partition grows each round
    - heap shrinks by one each iter (loses it to the partition)
4. Heapify the unsorted partition
5. Repeat

O(n log n) runtime complexity
"""

import unittest
import heapq


def heap_sort(numbers):
    """Can't figure how to do in-place with heapq."""

    unsorted = list(numbers)
    sorted_nums = []

    while unsorted:
        heapq.heapify(unsorted)
        sorted_nums.append(heapq.heappop(unsorted))

    return sorted_nums


class TestHeapSort(unittest.TestCase):
    """Test the functionality of heap_sort()."""

    def test_null(self):
        test_nums = []
        actual = heap_sort(test_nums)
        expected = []
        self.assertEqual(actual, expected)

    def test_singlet(self):
        test_nums = [3]
        actual = heap_sort(test_nums)
        expected = [3]
        self.assertEqual(actual, expected)

    def test_small_sorted(self):
        test_nums = [3, 5]
        actual = heap_sort(test_nums)
        expected = [3, 5]
        self.assertEqual(actual, expected)

    def test_small_unsorted(self):
        test_nums = [5, 3]
        actual = heap_sort(test_nums)
        expected = [3, 5]
        self.assertEqual(actual, expected)

    def test_sorted(self):
        test_nums = [2, 4, 6, 8]
        actual = heap_sort(test_nums)
        expected = [2, 4, 6, 8]
        self.assertEqual(actual, expected)

    def test_unsorted(self):
        test_nums = [8, 4, 2, 6]
        actual = heap_sort(test_nums)
        expected = [2, 4, 6, 8]
        self.assertEqual(actual, expected)

    def test_reversed(self):
        test_nums = [10, 7, 6, 4, 2, 1]
        actual = heap_sort(test_nums)
        expected = [1, 2, 4, 6, 7, 10]
        self.assertEqual(actual, expected)


unittest.main(verbosity=1)
