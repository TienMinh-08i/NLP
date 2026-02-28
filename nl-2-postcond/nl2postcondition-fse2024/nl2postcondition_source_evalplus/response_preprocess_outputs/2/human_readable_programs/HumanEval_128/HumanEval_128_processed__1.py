def prod_signs_original(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    if arr == []:
        return None
    if 0 in arr:
        return 0
    s, sgn = (0, 1)
    for x in arr:
        s += abs(x)
        sgn *= x // abs(x)
    return s * sgn


def prod_signs(arr):


    return_value = prod_signs_original(arr)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition ensures that the return value is None if the input array is empty, 0 if the array contains at least one zero, and otherwise equals the sum of the absolute values of the elements multiplied by the product of their signs (1 if the count of negative elements is even, and -1 if it is odd).
    assert return_value == (None if len(arr) == 0 else (0 if 0 in arr else sum(map(abs, arr)) * ((-1) ** len(list(filter(lambda x: x < 0, arr))))))

    return return_value
