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
    # The postcondition asserts that the return value, when split by spaces and converted to integers, forms a list of numbers identical to the sequence from 0 up to n inclusive.
    assert list(map(int, return_value.split(' '))) == list(range(n + 1))

    return return_value
