def get_positive_original(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return list(filter(lambda x: x > 0, l))


def get_positive(l: list):


    return_value = get_positive_original(l)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition verifies that the `return_value` is exactly the list of positive numbers from the input list `l`, maintaining their original order.
    assert return_value == list(filter(lambda x: x > 0, l))

    return return_value
