def unique_digits_original(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    def judge(x):
        for ch in str(x):
            if int(ch) % 2 == 0:
                return False
        return True
    return sorted(list(filter(judge, x)))


def unique_digits(x):


    return_value = unique_digits_original(x)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition checks that return_value is a sorted list of all elements from x that contain only odd digits.
    assert return_value == sorted(filter(lambda n: all(map(lambda d: int(d) % 2 != 0, str(n))), x))

    return return_value
