from typing import Any

def bubble_sort_iterative(collection: list[Any]) -> list[Any]:
    """
    Iterative implementation of the bubble sort algorithm.
    
    :param collection: List of comparable items.
    :return: The sorted list in ascending order.
    """
    length = len(collection)
    for i in range(length):
        swapped = False
        for j in range(1, length - i):
            if collection[j] < collection[j - 1]:
                collection[j], collection[j - 1] = collection[j - 1], collection[j]
                swapped = True
        if not swapped:  # If no elements were swapped, the list is sorted
            break
    return collection


def bubble_sort_recursive(collection: list[Any]) -> list[Any]:
    """
    Recursive implementation of the bubble sort algorithm.

    :param collection: List of comparable items.
    :return: The sorted list in ascending order.
    """
    length = len(collection)
    swapped = False
    for i in range(length - 1):
        if collection[i] > collection[i + 1]:
            collection[i], collection[i + 1] = collection[i + 1], collection[i]
            swapped = True

    # Base case: if no swaps were made, the list is sorted
    if not swapped:
        return collection
    # Recursive call
    return bubble_sort_recursive(collection)


if __name__ == "__main__":
    # Example usage
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    
    # Iterative sort
    print("Iterative Bubble Sort:")
    sorted_list_iter = bubble_sort_iterative(unsorted_list.copy())
    print(sorted_list_iter)

    # Recursive sort
    print("Recursive Bubble Sort:")
    sorted_list_rec = bubble_sort_recursive(unsorted_list.copy())
    print(sorted_list_rec)
