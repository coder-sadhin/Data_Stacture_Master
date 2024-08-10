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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
