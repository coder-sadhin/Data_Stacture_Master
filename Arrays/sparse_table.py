"""
Sparse table is a data structure that allows answering range queries on
a static number list, i.e. the elements do not change throughout all the queries.

The implementation below will solve the problem of Range Minimum Query:
Finding the minimum value of a subset [L..R] of a static number list.

Overall time complexity: O(nlogn)
Overall space complexity: O(nlogn)

Wikipedia link: https://en.wikipedia.org/wiki/Range_minimum_query
"""

from math import log2


def build_sparse_table(number_list: list[int]) -> list[list[int]]:
    """
    Precompute range minimum queries with power of two length and store the precomputed
    values in a table.

    >>> build_sparse_table([8, 1, 0, 3, 4, 9, 3])
    [[8, 1, 0, 3, 4, 9, 3], [1, 0, 0, 3, 4, 3, 0], [0, 0, 0, 3, 0, 0, 0]]
    >>> build_sparse_table([3, 1, 9])
    [[3, 1, 9], [1, 1, 0]]
    >>> build_sparse_table([])
    Traceback (most recent call last):
    ...
    ValueError: empty number list not allowed
    """
    if not number_list:
        raise ValueError("empty number list not allowed")

    length = len(number_list)
    # Initialise sparse_table -- sparse_table[j][i] represents the minimum value of the
    # subset of length (2 ** j) of number_list, starting from index i.

    # smallest power of 2 subset length that fully covers number_list
    row = int(log2(length)) + 1
    sparse_table = [[0 for i in range(length)] for j in range(row)]

    # minimum of subset of length 1 is that value itself
    for i, value in enumerate(number_list):
        sparse_table[0][i] = value
    j = 1

    # compute the minimum value for all intervals with size (2 ** j)
    while (1 << j) <= length:
        i = 0
        # while subset starting from i still have at least (2 ** j) elements
        while (i + (1 << j) - 1) < length:
            # split range [i, i + 2 ** j] and find minimum of 2 halves
            sparse_table[j][i] = min(
                sparse_table[j - 1][i + (1 << (j - 1))], sparse_table[j - 1][i]
            )
            i += 1
        j += 1
    return sparse_table


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(f"{query(build_sparse_table([3, 1, 9]), 2, 2) = }")
