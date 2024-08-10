def permute_recursive(nums: list[int]) -> list[list[int]]:
    """
    Return all permutations.

    >>> permute_recursive([1, 2, 3])
    [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]
    """
    

if __name__ == "__main__":
    import doctest

    result = permute_backtrack([1, 2, 3])
    print(result)
    doctest.testmod()
