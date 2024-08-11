"""
Given an array of integers and an integer k, find the kth largest element in the array.

https://stackoverflow.com/questions/251781
"""


def partition(arr: list[int], low: int, high: int) -> int:
    """
    Partitions list based on the pivot element.

    This function rearranges the elements in the input list 'elements' such that
    all elements greater than or equal to the chosen pivot are on the right side
    of the pivot, and all elements smaller than the pivot are on the left side.

    Args:
        arr: The list to be partitioned
        low: The lower index of the list
        high: The higher index of the list

    Returns:
        int: The index of pivot element after partitioning

        Examples:
        >>> partition([3, 1, 4, 5, 9, 2, 6, 5, 3, 5], 0, 9)
        4
        >>> partition([7, 1, 4, 5, 9, 2, 6, 5, 8], 0, 8)
        1
        >>> partition(['apple', 'cherry', 'date', 'banana'], 0, 3)
        2
        >>> partition([3.1, 1.2, 5.6, 4.7], 0, 3)
        1
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1



if __name__ == "__main__":
    import doctest

    doctest.testmod()
