from typing import List, Tuple

def find_closest_elements_original(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()
    min_diff = float('inf')
    min_pair = None
    for l, r in zip(numbers[:-1], numbers[1:]):
        diff = r - l
        if diff < min_diff:
            min_diff = diff
            min_pair = (l, r)
    return min_pair


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:


    return_value = find_closest_elements_original(numbers)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The return_value is a non-decreasing tuple of two elements from the input list such that their absolute difference is the minimum of all possible pairs of elements at distinct indices.
    assert return_value[0] <= return_value[1] and any(i != j and numbers[i] == return_value[0] and numbers[j] == return_value[1] for i in range(len(numbers)) for j in range(len(numbers))) and all(abs(numbers[i] - numbers[j]) >= return_value[1] - return_value[0] for i in range(len(numbers)) for j in range(len(numbers)) if i != j)

    return return_value
