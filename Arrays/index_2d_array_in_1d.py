"""
Retrieves the value of an 0-indexed 1D index from a 2D array.
There are two ways to retrieve value(s):

1. Index2DArrayIterator(matrix) -> Iterator[int]
This iterator allows you to iterate through a 2D array by passing in the matrix and
calling next(your_iterator). You can also use the iterator in a loop.
Examples:
list(Index2DArrayIterator(matrix))
set(Index2DArrayIterator(matrix))
tuple(Index2DArrayIterator(matrix))
sum(Index2DArrayIterator(matrix))
-5 in Index2DArrayIterator(matrix)

2. index_2d_array_in_1d(array: list[int], index: int) -> int
This function allows you to provide a 2D array and a 0-indexed 1D integer index,
and retrieves the integer value at that index.

Python doctests can be run using this command:
python3 -m doctest -v index_2d_array_in_1d.py
"""

from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class Index2DArrayIterator:
    matrix: list[list[int]]

    def __iter__(self) -> Iterator[int]:
        """
        >>> tuple(Index2DArrayIterator([[5], [-523], [-1], [34], [0]]))
        (5, -523, -1, 34, 0)
        >>> tuple(Index2DArrayIterator([[5, -523, -1], [34, 0]]))
        (5, -523, -1, 34, 0)
        >>> tuple(Index2DArrayIterator([[5, -523, -1, 34, 0]]))
        (5, -523, -1, 34, 0)
        >>> t = Index2DArrayIterator([[5, 2, 25], [23, 14, 5], [324, -1, 0]])
        >>> tuple(t)
        (5, 2, 25, 23, 14, 5, 324, -1, 0)
        >>> list(t)
        [5, 2, 25, 23, 14, 5, 324, -1, 0]
        >>> sorted(t)
        [-1, 0, 2, 5, 5, 14, 23, 25, 324]
        >>> tuple(t)[3]
        23
        >>> sum(t)
        397
        >>> -1 in t
        True
        >>> t = iter(Index2DArrayIterator([[5], [-523], [-1], [34], [0]]))
        >>> next(t)
        5
        >>> next(t)
        -523
        """
        for row in self.matrix:
            yield from row



if __name__ == "__main__":
    import doctest

    doctest.testmod()
