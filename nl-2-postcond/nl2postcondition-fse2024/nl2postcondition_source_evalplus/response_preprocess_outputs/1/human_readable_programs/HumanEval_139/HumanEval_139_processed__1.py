def special_factorial_original(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    fac, ans = (1, 1)
    for i in range(2, n + 1):
        fac *= i
        ans *= fac
    return ans


def special_factorial(n):


    return_value = special_factorial_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition asserts that the `return_value` is equal to the product of factorials from 1! up to n!.
    # This is calculated by dynamically importing `functools` and using `reduce` to first compute each factorial (k!) and then to compute the product of these factorials.
    assert return_value == __import__('functools').reduce(lambda acc, i: acc * (__import__('functools').reduce(lambda x, y: x * y, range(1, i + 1), 1)), range(1, n + 1), 1)
    

    return return_value
