def unique_original(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))


def unique(l: list):


    return_value = unique_original(l)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition asserts that the returned list contains only unique elements, is sorted in non-decreasing order, and contains exactly the same unique elements as the input list.
    assert len(return_value) == len(set(return_value)) and \
           (len(return_value) <= 1 or all(return_value[i] <= return_value[i+1] for i in range(len(return_value) - 1))) and \
           set(return_value) == set(l)
    

    return return_value
