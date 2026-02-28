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
    # This postcondition checks that if both inputs `a` and `b` are zero, the `return_value` is 0. Otherwise, it asserts that `return_value` is a positive integer that divides both `a` and `b`, and that no integer larger than `return_value` also divides both `a` and `b`.
    assert (a == 0 and b == 0 and return_value == 0) or \
           (return_value > 0 and \
            a % return_value == 0 and \
            b % return_value == 0 and \
            all(not (a % k == 0 and b % k == 0) \
                for k in range(return_value + 1, max(abs(a), abs(b)) + 1)))

    return return_value
