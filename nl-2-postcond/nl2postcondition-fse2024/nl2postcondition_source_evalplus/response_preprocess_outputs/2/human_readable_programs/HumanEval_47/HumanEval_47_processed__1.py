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
    # The postcondition verifies that the return_value is the middle element of the sorted list l if its length is odd, or the average of the two middle elements if its length is even.
    assert return_value == (sorted(l)[len(l) // 2] if len(l) % 2 == 1 else (sorted(l)[len(l) // 2 - 1] + sorted(l)[len(l) // 2]) / 2)

    return return_value
