from typing import List

def intersperse_original(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    res = []
    for i in range(len(numbers)):
        res.append(numbers[i])
        if i != len(numbers) - 1:
            res.append(delimeter)
    return res


def intersperse(numbers: List[int], delimeter: int) -> List[int]:


    return_value = intersperse_original(numbers, delimeter)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks that:
    # 1. The length of the return value is correct: if 'numbers' has N elements, 'return_value' has N + max(0, N-1) elements.
    # 2. All elements from the original 'numbers' list appear at even indices in 'return_value', in their original order.
    # 3. The 'delimeter' appears at all odd indices in 'return_value' (if 'numbers' has more than one element).
    assert len(return_value) == (len(numbers) + max(0, len(numbers) - 1)) and \
           all(return_value[2*i] == numbers[i] for i in range(len(numbers))) and \
           all(return_value[2*i + 1] == delimeter for i in range(len(numbers) - 1))
    

    return return_value
