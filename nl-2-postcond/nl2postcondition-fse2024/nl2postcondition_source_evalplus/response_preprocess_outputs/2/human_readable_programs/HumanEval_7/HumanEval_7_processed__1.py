from typing import List

def filter_by_substring_original(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return list(filter(lambda s: substring in s, strings))


def filter_by_substring(strings: List[str], substring: str) -> List[str]:


    return_value = filter_by_substring_original(strings, substring)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition verifies that return_value contains all strings from the input list that include the given substring, maintaining their original order.
    assert return_value == list(filter(lambda s: substring in s, strings))
    

    return return_value
