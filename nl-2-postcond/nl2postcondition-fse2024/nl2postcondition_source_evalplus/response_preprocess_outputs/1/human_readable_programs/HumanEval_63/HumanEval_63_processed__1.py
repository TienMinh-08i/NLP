def fibfib_original(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    a, b, c = (0, 0, 1)
    for _ in range(3, n + 1):
        a, b, c = (b, c, a + b + c)
    return c


def fibfib(n: int):


    return_value = fibfib_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    import functools
    
    # The postcondition verifies that the returned value matches the definition of the FibFib sequence.
    # It checks the base cases for n=0, 1, 2 directly. For n >= 3, it re-computes the Nth FibFib
    # number using functools.reduce, simulating the iterative sequence generation (a, b, c) -> (b, c, a+b+c).
    assert (n == 0 and return_value == 0) or \
           (n == 1 and return_value == 0) or \
           (n == 2 and return_value == 1) or \
           (n > 2 and return_value == functools.reduce(
               lambda state, _: (state[1], state[2], state[0] + state[1] + state[2]),
               range(n - 2),  # Iterates (n-2) times to reach fibfib_original(n) from fibfib_original(2)
               (0, 0, 1)      # Initial state (fibfib_original(0), fibfib_original(1), fibfib_original(2))
           )[2])
    

    return return_value
