def largest_divisor_original(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(2, n):
        if n % i == 0:
            return n // i
    return 1


def largest_divisor(n: int) -> int:


    return_value = largest_divisor_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition asserts that the returned value `return_value` is a divisor of `n`, is strictly smaller than `n`, and is the largest such number among all positive integers.
    assert n % return_value == 0 and return_value < n and all(return_value >= k for k in filter(lambda x: n % x == 0, range(1, n)))
    

    return return_value
