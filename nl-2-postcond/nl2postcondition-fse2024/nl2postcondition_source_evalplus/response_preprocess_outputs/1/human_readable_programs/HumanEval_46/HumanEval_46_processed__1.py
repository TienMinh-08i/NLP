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
    
    
    # The postcondition verifies that the returned value matches the n-th element of the Fib4 sequence.
    # It computes the sequence iteratively up to n by encapsulating the stateful generation within nested lambdas,
    # using the `map` function to apply a side-effecting lambda that appends new Fib4 numbers to a list,
    # and then extracts the n-th element from the generated list. This approach handles all non-negative n.
    assert (lambda n_val: \
                # This inner lambda initializes the base sequence values [fib4_original(0), fib4_original(1), fib4_original(2), fib4_original(3)].
                # This list will be mutated by the map function to extend the sequence.
                (lambda fibs_list: \
                    # The 'list(...)' call forces the evaluation of the map object, which in turn executes
                    # the inner lambda for each 'i' in the range. The inner lambda's side effect is to
                    # append the next Fib4 number to 'fibs_list'.
                    # The outer tuple ensures that both the side effect (list population) happens
                    # and the final desired value (fibs_list[n_val]) is available for selection.
                    (list(map(lambda i: fibs_list.append(sum(fibs_list[i-4:i])), range(4, n_val + 1))), \
                     fibs_list[n_val]) \
                )([0, 0, 2, 0]) \
            )[1])(n) == return_value
    

    return return_value
