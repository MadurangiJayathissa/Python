def cycle_sort(array: list) -> list:
    """
    Cycle sort algorithm to sort an array in-place.

    Example usage:
    >>> cycle_sort([4, 3, 2, 1])
    [1, 2, 3, 4]

    >>> cycle_sort([-4, 20, 0, -50, 100, -1])
    [-50, -4, -1, 0, 20, 100]

    >>> cycle_sort([-.1, -.2, 1.3, -.8])
    [-0.8, -0.2, -0.1, 1.3]

    >>> cycle_sort([])
    []
    """
    array_len = len(array)

    for cycle_start in range(array_len - 1):
        item = array[cycle_start]

        # Find the position where the item should go
        pos = cycle_start
        for i in range(cycle_start + 1, array_len):
            if array[i] < item:
                pos += 1

        # If the item is already in the correct position, continue
        if pos == cycle_start:
            continue

        # Otherwise, put the item at its correct position
        while item == array[pos]:
            pos += 1

        array[pos], item = item, array[pos]

        # Continue the cycle to move all misplaced items to their correct positions
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, array_len):
                if array[i] < item:
                    pos += 1

            while item == array[pos]:
                pos += 1

            array[pos], item = item, array[pos]

    return array



if __name__ == "__main__":
    assert cycle_sort([4, 5, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert cycle_sort([0, 1, -10, 15, 2, -2]) == [-10, -2, 0, 1, 2, 15]

