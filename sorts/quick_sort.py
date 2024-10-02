from __future__ import annotations

from random import randrange


def quick_sort(array):
    """
    Sorts an array using the Quick Sort algorithm.
    
    :param array: List of elements to be sorted.
    :return: Sorted list.
    
    Examples:
    >>> quick_sort([3, 6, 8, 10, 1, 2, 1])
    [1, 1, 2, 3, 6, 8, 10]
    >>> quick_sort([1, 3, 9, 8, 2, 7, 5])
    [1, 2, 3, 5, 7, 8, 9]
    >>> quick_sort([10, 7, 8, 9, 1, 5])
    [1, 5, 7, 8, 9, 10]
    """
    
    if len(array) <= 1:
        return array
    else:
        pivot = array[len(array) // 2]  # Choose the middle element as the pivot
        left = [x for x in array if x < pivot]  # Elements less than pivot
        middle = [x for x in array if x == pivot]  # Elements equal to pivot
        right = [x for x in array if x > pivot]  # Elements greater than pivot
        return quick_sort(left) + middle + quick_sort(right)


# Test the function
if __name__ == "__main__":
    import doctest
    doctest.testmod()

    user_input = input("Enter numbers separated by commas: ").strip()
    unsorted_list = [int(x) for x in user_input.split(",")]
    print(f"Sorted list: {quick_sort(unsorted_list)}")
