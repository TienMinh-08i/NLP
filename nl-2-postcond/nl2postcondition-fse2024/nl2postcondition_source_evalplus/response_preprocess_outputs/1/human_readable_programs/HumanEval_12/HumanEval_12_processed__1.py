from typing import List, Optional

def longest_original(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    maxlen = max((len(x) for x in strings))
    for s in strings:
        if len(s) == maxlen:
            return s


def longest(strings: List[str]) -> Optional[str]:


    return_value = longest_original(strings)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition asserts that if the input list 'strings' is empty, the return value must be None.
    # Otherwise, if 'strings' is not empty, it asserts that the return value is one of the strings in the input list,
    # that its length is the maximum length among all strings in the list,
    # and that no string appearing before it in the original list has the same maximum length.
    assert (return_value is None and not strings) or \
           (strings and \
            return_value in strings and \
            len(return_value) == max(len(s) for s in strings) and \
            all(len(s) < len(return_value) for s in strings[:strings.index(return_value)]))
    

    return return_value
