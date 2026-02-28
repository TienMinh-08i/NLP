def same_chars_original(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    return set(s0) == set(s1)


def same_chars(s0: str, s1: str):


    return_value = same_chars_original(s0, s1)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition asserts that the returned value is True if and only if the set of unique characters in the first string is equal to the set of unique characters in the second string.
    assert return_value == (set(s0) == set(s1))

    return return_value
