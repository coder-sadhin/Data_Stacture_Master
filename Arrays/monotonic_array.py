# https://leetcode.com/problems/monotonic-array/
def is_monotonic(nums: list[int]) -> bool:
    """
    Check if a list is monotonic.

    >>> is_monotonic([1, 2, 2, 3])
    True
    >>> is_monotonic([6, 5, 4, 4])
    True
    >>> is_monotonic([1, 3, 2])
    False
    """
   


# Test the function with your examples
if __name__ == "__main__":
    # Test the function with your examples
    print(is_monotonic([1, 2, 2, 3]))  # Output: True
    print(is_monotonic([6, 5, 4, 4]))  # Output: True
    print(is_monotonic([1, 3, 2]))  # Output: False
