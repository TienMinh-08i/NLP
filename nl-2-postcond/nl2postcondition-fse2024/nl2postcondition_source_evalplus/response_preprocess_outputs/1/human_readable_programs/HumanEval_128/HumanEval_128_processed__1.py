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
    # The postcondition asserts that if the input array `arr` is empty, the `return_value` must be `None`.
    # If `arr` contains `0`, the `return_value` must be `0`.
    # Otherwise (if `arr` is not empty and does not contain `0`), the `return_value` must be the sum of the absolute values of its elements, multiplied by `1` if there is an even number of negative elements, and by `-1` if there is an odd number of negative elements.
    assert (len(arr) == 0 and return_value is None) or \
           (0 in arr and return_value == 0) or \
           (len(arr) > 0 and 0 not in arr and \
            return_value == sum(map(abs, arr)) * (1 if len(list(filter(lambda x: x < 0, arr))) % 2 == 0 else -1))

    return return_value
