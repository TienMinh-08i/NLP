def is_simple_power_original(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    if x == 1:
        return True
    if n == 0:
        return x == 0
    if n == 1:
        return x == 1
    if n == -1:
        return abs(x) == 1
    p = n
    while abs(p) <= abs(x):
        if p == x:
            return True
        p = p * n
    return False


def is_simple_power(x, n):


    return_value = is_simple_power_original(x, n)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition verifies that the return_value is true if and only if x is a simple power of n.
    # A number x is a simple power of n if there exists a non-negative integer k such that n**k == x,
    # and for all intermediate powers n**j (where 1 <= j < k), their absolute values do not exceed abs(x).
    # This captures the specific behavior of the provided function, including its handling of edge cases
    # for x=1, n=0, n=1, n=-1, and the loop termination condition for other cases.
    assert return_value == (
        # Case 1: If x is 1, it's always a simple power (n^0 = 1).
        (x == 1) or
        # Case 2: If n is 0, x must also be 0 (0^k = 0 for k > 0).
        (n == 0 and x == 0) or
        # Case 3: If n is 1, x must also be 1 (1^k = 1).
        (n == 1 and x == 1) or
        # Case 4: If n is -1, x must be 1 or -1 ((-1)^even = 1, (-1)^odd = -1).
        (n == -1 and abs(x) == 1) or
        # Case 5: General case for other values of n and x.
        # We check if there's an integer k >= 1 such that n**k == x.
        # The `all` condition ensures that `abs(n**j)` for intermediate powers `j` (1 <= j < k)
        # does not exceed `abs(x)`, mimicking the `while abs(p) <= abs(x)` loop behavior of the function.
        # MAX_K=64 is a safe upper bound for the exponent, sufficient for typical integer ranges.
        (n not in (0, 1, -1) and
         any(n**k == x and all(abs(n**j) <= abs(x) for j in range(1, k)) for k in range(1, 64)))
    )

    return return_value
