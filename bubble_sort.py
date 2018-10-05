"""
Implementation for bubble sort.

Worst case: О(n**2)
    Reverse order
Avg case: О(n**2)
    Barely-sorted/random
Best case: O(n)
    Already sorted

Although the algorithm is simple, it is too slow and impractical for most
problems, especially as the input gets large and if the input is nearly (or
totally) in reverse order.
"""


def bubble_sort(numbers):
    """Sort a list of numbers using the bubble sort algorithm."""
    in_order = False
    swaps = False
    while not in_order:
        swaps = False
        for indx in range(len(numbers) - 1):
            if numbers[indx + 1] < numbers[indx]:
                swaps = True
                lesser = numbers[indx + 1]
                numbers[indx + 1] = numbers[indx]
                numbers[indx] = lesser

        if swaps == False:
            in_order = True

    return numbers


if __name__ == '__main__':
    test1 = [2, 8, 4, 5, 99, 12, 6]
    test2 = [99, 88, 54, 45, 29, 12, 6]
    print(bubble_sort(test1))
    print(bubble_sort(test2))