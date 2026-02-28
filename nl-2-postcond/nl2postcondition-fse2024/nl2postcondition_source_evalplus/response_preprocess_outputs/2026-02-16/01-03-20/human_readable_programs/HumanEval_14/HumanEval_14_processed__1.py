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
    # The postcondition checks that the returned list's length is equal to the input string's length, and that each element at index `i` in the list is the prefix of the input string from its beginning up to `i+1` characters.
    assert len(return_value) == len(string) and \
           all(return_value[i] == string[:i+1] for i in range(len(string)))

    return return_value
