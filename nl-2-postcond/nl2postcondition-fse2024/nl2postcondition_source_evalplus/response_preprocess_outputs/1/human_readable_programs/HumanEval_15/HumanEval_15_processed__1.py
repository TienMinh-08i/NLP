def string_sequence_original(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return ' '.join(map(str, range(n + 1)))


def string_sequence(n: int) -> str:


    return_value = string_sequence_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks that the return value is a string,
    # that it contains space-delimited numbers from 0 up to n,
    # and that there are exactly n+1 such numbers, each corresponding to its index.
    assert (isinstance(return_value, str) and
            len(return_value.split(' ')) == n + 1 and
            all(int(num_str) == i for i, num_str in enumerate(return_value.split(' '))))
    

    return return_value
