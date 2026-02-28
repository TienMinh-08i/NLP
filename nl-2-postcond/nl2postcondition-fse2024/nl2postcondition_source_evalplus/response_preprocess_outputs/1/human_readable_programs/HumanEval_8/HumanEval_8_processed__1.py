from typing import List, Tuple

def sum_product_original(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    s, p = (0, 1)
    for number in numbers:
        s += number
        p *= number
    return (s, p)


def sum_product(numbers: List[int]) -> Tuple[int, int]:


    return_value = sum_product_original(numbers)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition verifies that the first element of the return value is the sum of all integers in the input list,
    # and the second element is the product of all integers. It correctly handles an empty list, where the sum is 0 and the product is 1.
    from functools import reduce
    assert return_value[0] == sum(numbers) and return_value[1] == reduce(lambda x, y: x * y, numbers, 1)
    

    return return_value
