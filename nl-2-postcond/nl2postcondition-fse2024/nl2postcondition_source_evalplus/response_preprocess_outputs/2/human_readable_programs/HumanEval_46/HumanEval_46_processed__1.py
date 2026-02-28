def fib4_original(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        a, b, c, d = (0, 0, 2, 0)
        for i in range(4, n + 1):
            a, b, c, d = (b, c, d, a + b + c + d)
        return d


def fib4(n: int):


    return_value = fib4_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition verifies that return_value matches the n-th term of the Fib4 sequence by using functools.reduce to iteratively compute the sum of the four preceding terms, starting from the initial sequence values for n=0, 1, 2, and 3.
    assert return_value == ((0, 0, 2, 0)[n] if n < 4 else __import__('functools').reduce(lambda s, _: (s[1], s[2], s[3], sum(s)), range(4, n + 1), (0, 0, 2, 0))[-1])

    return return_value
