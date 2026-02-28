def greatest_common_divisor_original(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    def query_gcd(a: int, b: int) -> int:
        return a if b == 0 else query_gcd(b, a % b)
    return query_gcd(a, b)


def greatest_common_divisor(a: int, b: int) -> int:


    return_value = greatest_common_divisor_original(a, b)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The return_value is a common divisor of a and b, and no integer with an absolute value greater than that of return_value is a common divisor of both a and b.
    assert (a == 0 and b == 0 and return_value == 0) or ((a != 0 or b != 0) and return_value != 0 and a % return_value == 0 and b % return_value == 0 and all(a % i != 0 or b % i != 0 for i in range(abs(return_value) + 1, max(abs(a), abs(b)) + 1)))

    return return_value
