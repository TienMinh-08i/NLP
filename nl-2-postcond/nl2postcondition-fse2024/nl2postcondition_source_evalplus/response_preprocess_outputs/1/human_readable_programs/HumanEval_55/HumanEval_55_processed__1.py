def fib_original(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n == 0:
        return 0
    if n <= 2:
        return 1
    a, b = (1, 1)
    for _ in range(3, n + 1):
        a, b = (b, a + b)
    return b


def fib(n: int):


    return_value = fib_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    import functools
    
    # Postcondition: Checks if the returned value matches the n-th Fibonacci number.
    # It handles the base case for n=0 directly. For n >= 1, it iteratively computes
    # the n-th Fibonacci number using functools.reduce, mimicking the sequence generation,
    # and compares it with the return_value.
    assert (n == 0 and return_value == 0) or \
           (n >= 1 and functools.reduce(lambda acc, _: (acc[1], acc[0] + acc[1]), range(n - 1), (0, 1))[1] == return_value)
    

    return return_value
