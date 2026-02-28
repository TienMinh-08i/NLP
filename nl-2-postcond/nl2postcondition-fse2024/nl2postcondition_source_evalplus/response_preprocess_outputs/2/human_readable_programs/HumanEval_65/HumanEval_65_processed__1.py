def circular_shift_original(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    s = str(x)
    if shift > len(s):
        return s[::-1]
    shift %= len(s)
    if shift == 0:
        return s
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]


def circular_shift(x, shift):


    return_value = circular_shift_original(x, shift)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition ensures that if the shift is greater than the number of digits in x, the return value is the string of digits reversed; otherwise, it is the string of digits circularly shifted right by shift modulo the number of digits.
    assert return_value == (str(x)[::-1] if shift > len(str(x)) else str(x)[len(str(x)) - (shift % len(str(x))):] + str(x)[:len(str(x)) - (shift % len(str(x)))])
    

    return return_value
