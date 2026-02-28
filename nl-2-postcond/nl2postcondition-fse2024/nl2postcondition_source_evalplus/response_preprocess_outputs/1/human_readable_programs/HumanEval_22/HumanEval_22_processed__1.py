from typing import List, Any

def filter_integers_original(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return list(filter(lambda x: type(x) == int, values))


def filter_integers(values: List[Any]) -> List[int]:


    return_value = filter_integers_original(values)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition asserts that the `return_value` is a list containing only integers, and that it is exactly the sequence of integer elements found in the `values` input list, preserving their original order.
    assert return_value == list(filter(lambda x: type(x) == int, values))

    return return_value
