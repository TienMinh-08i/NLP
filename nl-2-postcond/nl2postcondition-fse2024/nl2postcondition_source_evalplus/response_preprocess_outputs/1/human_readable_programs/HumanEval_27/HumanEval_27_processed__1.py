def flip_case_original(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(map(lambda x: x.swapcase(), string))


def flip_case(string: str) -> str:


    return_value = flip_case_original(string)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    
    # The postcondition asserts that the length of the returned string is equal to the length of the input string,
    # and for every character in the input string, its corresponding character in the returned string is its case-flipped version.
    assert len(string) == len(return_value) and all(original_char.swapcase() == flipped_char for original_char, flipped_char in zip(string, return_value))
    

    return return_value
