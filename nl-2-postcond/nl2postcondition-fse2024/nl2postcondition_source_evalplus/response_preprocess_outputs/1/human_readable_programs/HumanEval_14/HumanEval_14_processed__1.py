from typing import List

def all_prefixes_original(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i + 1] for i in range(len(string))]


def all_prefixes(string: str) -> List[str]:


    return_value = all_prefixes_original(string)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition asserts that the length of the returned list equals the length of the input string, and that each element in the returned list is a prefix of the input string, with the i-th element (0-indexed) being the prefix of length i+1.
    assert len(return_value) == len(string) and all(return_value[i] == string[:i + 1] for i in range(len(string)))

    return return_value
