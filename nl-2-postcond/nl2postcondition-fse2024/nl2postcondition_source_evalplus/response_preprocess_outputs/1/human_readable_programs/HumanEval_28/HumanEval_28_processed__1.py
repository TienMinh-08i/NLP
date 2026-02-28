from typing import List

def concatenate_original(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)


def concatenate(strings: List[str]) -> str:


    return_value = concatenate_original(strings)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition asserts that the return value is exactly the concatenation of the input strings,
    # by checking if it matches a regular expression pattern built from the escaped input strings.
    import re
    assert re.fullmatch("".join(map(re.escape, strings)), return_value) is not None
    

    return return_value
