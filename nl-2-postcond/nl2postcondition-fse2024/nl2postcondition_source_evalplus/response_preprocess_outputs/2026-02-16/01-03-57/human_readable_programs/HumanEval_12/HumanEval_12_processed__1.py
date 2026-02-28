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
    # The postcondition asserts that if the input list is empty, the return value is None. Otherwise, it asserts that the return value is a string from the input list, it has the maximum length among all strings in the list, and it is the first string in the list that achieves this maximum length.
    assert (not strings and return_value is None) or \
           (strings and return_value is not None and \
            return_value in strings and \
            len(return_value) == max(map(len, strings)) and \
            all(len(s_prev) < len(return_value) \
                for i, s_prev in enumerate(strings) \
                if i < next(j for j, s_curr in enumerate(strings) if s_curr == return_value)))

    return return_value
