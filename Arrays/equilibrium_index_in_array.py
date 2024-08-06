"""
Find the Equilibrium Index of an Array.
Reference: https://www.geeksforgeeks.org/equilibrium-index-of-an-array/

Python doctest can be run with the following command:
python -m doctest -v equilibrium_index_in_array.py

Given a sequence arr[] of size n, this function returns
an equilibrium index (if any) or -1 if no equilibrium index exists.

The equilibrium index of an array is an index such that the sum of
elements at lower indexes is equal to the sum of elements at higher indexes.



Example Input:
arr = [-7, 1, 5, 2, -4, 3, 0]
Output: 3

"""




if __name__ == "__main__":
    import doctest

    doctest.testmod()
