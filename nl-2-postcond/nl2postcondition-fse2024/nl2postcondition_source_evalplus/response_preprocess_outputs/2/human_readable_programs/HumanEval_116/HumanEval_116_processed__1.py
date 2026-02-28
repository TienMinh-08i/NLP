def sort_array_original(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    from functools import cmp_to_key

    def cmp(x: int, y: int) -> int:
        x1 = len(list(filter(lambda ch: ch == '1', bin(x))))
        y1 = len(list(filter(lambda ch: ch == '1', bin(y))))
        if x1 != y1:
            return x1 - y1
        return x - y
    return sorted(arr, key=cmp_to_key(cmp))


def sort_array(arr):


    return_value = sort_array_original(arr)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The return_value must be a permutation of the input arr and must be sorted in ascending order based on the number of '1's in the binary representation of each element, with ties broken by the decimal value in ascending order.
    assert len(return_value) == len(arr) and sorted(return_value) == sorted(arr) and all((len(list(filter(lambda ch: ch == '1', bin(return_value[i])))), return_value[i]) <= (len(list(filter(lambda ch: ch == '1', bin(return_value[i + 1])))), return_value[i + 1]) for i in range(len(return_value) - 1))

    return return_value
