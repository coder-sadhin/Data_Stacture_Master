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



if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(f"{query(build_sparse_table([3, 1, 9]), 2, 2) = }")
