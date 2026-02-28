def change_base_original(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:
        return '0'
    ret = ''
    while x != 0:
        ret = str(x % base) + ret
        x //= base
    return ret


def change_base(x: int, base: int):


    return_value = change_base_original(x, base)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition asserts that the `return_value` is a valid string representation of `x` in the given `base`.
    # This means that all digits in `return_value` are valid for the `base` (i.e., less than `base`), and when `return_value` is converted back to base 10, it equals the original number `x`.
    # It also ensures that there are no leading zeros, unless `x` itself is 0.
    assert (x == 0 and return_value == "0") or \
           (x > 0 and \
            len(return_value) > 0 and \
            return_value[0] != '0' and \
            all(int(digit) < base for digit in return_value) and \
            sum(int(digit) * (base ** power) for power, digit in enumerate(reversed(return_value))) == x)

    return return_value
