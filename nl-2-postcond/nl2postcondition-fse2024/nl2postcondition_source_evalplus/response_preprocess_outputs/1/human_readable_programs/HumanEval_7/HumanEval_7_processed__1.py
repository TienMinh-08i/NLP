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
    # This postcondition ensures two things: first, that every string in the returned list actually contains the specified substring; and second, that every string from the original input list that contains the substring is present in the returned list, effectively verifying that the returned list is exactly the filtered subset.
    assert all(substring in s for s in return_value) and all(s in return_value for s in strings if substring in s)

    return return_value
