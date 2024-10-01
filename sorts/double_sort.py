from typing import Any, List


def double_sort(collection: List[Any]) -> List[Any]:
    """Sorts an array using a double bubble sort algorithm,
    sorting both from left to right and right to left.
    
    :param collection: A mutable ordered sequence of elements
    :return: The same collection in ascending order
    
    Examples:
    >>> double_sort([-1, -2, -3, -4, -5, -6, -7])
    [-7, -6, -5, -4, -3, -2, -1]
    >>> double_sort([])
    []
    >>> double_sort([-1, -2, -3, -4, -5, -6])
    [-6, -5, -4, -3, -2, -1]
    >>> double_sort([-3, 10, 16, -42, 29]) == sorted([-3, 10, 16, -42, 29])
    True
    """
    no_of_elements = len(collection)
    
    for _ in range(int((no_of_elements - 1) / 2) + 1):
        for j in range(no_of_elements - 1):
            # Sort from left to right (forwards)
            if collection[j + 1] < collection[j]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
            
            # Sort from right to left (backwards)
            if collection[no_of_elements - 1 - j] < collection[no_of_elements - 2 - j]:
                collection[no_of_elements - 1 - j], collection[no_of_elements - 2 - j] = (
                    collection[no_of_elements - 2 - j], collection[no_of_elements - 1 - j]
                )
    
    return collection


if __name__ == "__main__":
    # Allow the user to input the elements of the list on one line
    unsorted = [int(x) for x in input("Enter the list to be sorted: ").split() if x]
    print("The sorted list is:")
    print(double_sort(unsorted))
