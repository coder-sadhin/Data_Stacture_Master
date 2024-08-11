"""
https://www.enjoyalgorithms.com/blog/median-of-two-sorted-arrays
"""


def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    """
    Find the median of two arrays.

    Args:
        nums1: The first array.
        nums2: The second array.

    Returns:
    The median of the two arrays.

    Examples:
        >>> find_median_sorted_arrays([1, 3], [2])
        2.0

        >>> find_median_sorted_arrays([1, 2], [3, 4])
        2.5

        >>> find_median_sorted_arrays([0, 0], [0, 0])
        0.0

        >>> find_median_sorted_arrays([], [])
        Traceback (most recent call last):
            ...
        ValueError: Both input arrays are empty.

        >>> find_median_sorted_arrays([], [1])
        1.0

        >>> find_median_sorted_arrays([-1000], [1000])
        0.0

        >>> find_median_sorted_arrays([-1.1, -2.2], [-3.3, -4.4])
        -2.75
    """
    


if __name__ == "__main__":
    import doctest

    doctest.testmod()
