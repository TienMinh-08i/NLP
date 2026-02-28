from typing import List

def string_xor_original(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join((str(int(a[i]) ^ int(b[i])) for i in range(len(a))))


def string_xor(a: str, b: str) -> str:


    return_value = string_xor_original(a, b)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition verifies that return_value has the same length as input a and that each character is '1' if the corresponding characters in a and b are different, and '0' if they are the same.
    assert len(return_value) == len(a) and all(res == ('1' if x != y else '0') for x, y, res in zip(a, b, return_value))

    return return_value
