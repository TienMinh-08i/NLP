def median_original(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_l = sorted(l)
    if len(l) % 2 == 1:
        return sorted_l[len(l) // 2]
    else:
        return (sorted_l[len(l) // 2 - 1] + sorted_l[len(l) // 2]) / 2


def median(l: list):


    return_value = median_original(l)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition asserts that for a non-empty list, the return value is a median.
    # This means that at least half of the elements in the input list are less than or equal to the return value,
    # and at least half are greater than or equal to the return value.
    # Specifically, for a list of length N, at least ceil(N/2) elements must satisfy each condition.
    # ceil(N/2) can be calculated as (N + 1) // 2 for positive integers N.
    assert len(l) > 0 and \
           len(list(filter(lambda x: x <= return_value, l))) >= (len(l) + 1) // 2 and \
           len(list(filter(lambda x: x >= return_value, l))) >= (len(l) + 1) // 2

    return return_value
