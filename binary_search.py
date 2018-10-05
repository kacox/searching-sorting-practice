"""
Binary search implementations.

    1) Iterative
    2) Recursive
"""

list_a = []
list_b = [2, 5, 6, 8, 12, 33]
list_c = [1, 5, 6, 10, 12, 22, 33]


# ITERATIVE
def binary_search_iter(sorted_list, query):
    first = 0
    last = len(sorted_list) - 1
    found = False

    while first <= last and not found:
        middle = (last + first) // 2
        if sorted_list[middle] == query:
            found = True
        elif sorted_list[middle] < query:
            first = middle + 1
        elif sorted_list[middle] > query:
            last = middle - 1

    return found

# RECURSIVE
def binary_search_recur(sorted_list, query):
    if len(sorted_list) == 0:
        return False

    middle = (len(sorted_list) - 1) // 2

    if sorted_list[middle] == query:
        return True
    elif sorted_list[middle] < query:
        return binary_search_recur(sorted_list[middle + 1:], query)
    elif sorted_list[middle] > query:
        return binary_search_recur(sorted_list[:middle], query)


if __name__ == '__main__':
    # iter tests
    print(binary_search_iter(list_a, 1))
    print(binary_search_iter(list_b, 33))
    print(binary_search_iter(list_b, 40))
    print(binary_search_iter(list_c, 5))
    print(binary_search_iter(list_c, -2), "\n")

    # recursive tests
    print(binary_search_recur(list_a, 1))
    print(binary_search_recur(list_b, 33))
    print(binary_search_recur(list_b, 40))
    print(binary_search_recur(list_c, 5))
    print(binary_search_recur(list_c, -2))