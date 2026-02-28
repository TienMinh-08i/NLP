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
    # This postcondition verifies two properties of the sort_array function's return value:
    # 1. It is a permutation of the input array `arr`, meaning it contains the same elements with the same frequencies.
    # 2. It is sorted according to the specified criteria: primarily by the count of '1's in the binary representation
    #    (as defined by the function's internal `cmp` logic) in ascending order, and secondarily by the decimal value
    #    in ascending order for elements with an equal count of '1's.
    assert (len(return_value) == len(arr) and
            all(map(lambda x: return_value.count(x) == arr.count(x), set(arr))) and
            all(map(lambda i:
                    (lambda ones_x, ones_y, x, y:
                        (ones_x < ones_y) or (ones_x == ones_y and x <= y)
                    )(len(list(filter(lambda ch: ch == "1", bin(return_value[i])))),
                      len(list(filter(lambda ch: ch == "1", bin(return_value[i+1])))),
                      return_value[i],
                      return_value[i+1]),
                    range(len(return_value) - 1))))

    return return_value
