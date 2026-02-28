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
    # The postcondition asserts that the `return_value` is a sorted list containing exactly those elements from the input list `x` that do not have any even digits.
    assert return_value == sorted(list(filter(lambda num: all(int(digit) % 2 != 0 for digit in str(num)), x)))

    return return_value
