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
    
    # The postcondition asserts that the length of the returned string is equal to the length of the input strings,
    # and each character in the returned string is the binary XOR result of the corresponding characters in the input strings.
    assert len(return_value) == len(a) and \
           all(return_value[i] == str(int(a[i]) ^ int(b[i])) for i in range(len(a)))
    

    return return_value
