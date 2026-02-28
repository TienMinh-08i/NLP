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
    
    # The postcondition ensures that return_value contains the same set of elements as the input list l and is sorted in strictly ascending order, which also guarantees uniqueness.
    assert set(return_value) == set(l) and all(return_value[i] < return_value[i + 1] for i in range(len(return_value) - 1))
    

    return return_value
