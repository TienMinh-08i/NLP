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
    
    # The n-th Fibonacci number is equal to the sum of the binomial coefficients (n-k-1 choose k) for k from 0 to floor((n-1)/2).
    assert return_value == sum(__import__('math').comb(n - k - 1, k) for k in range((n + 1) // 2))
    

    return return_value
