from typing import List

def factorize_original(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    import math
    fact = []
    i = 2
    while i <= int(math.sqrt(n) + 1):
        if n % i == 0:
            fact.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        fact.append(n)
    return fact


def factorize(n: int) -> List[int]:


    return_value = factorize_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition verifies that the product of the prime factors in return_value is equal to n, the factors are in non-decreasing order, and each factor is a prime number.
    assert __import__('math').prod(return_value) == n and return_value == sorted(return_value) and all(x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1)) for x in return_value)

    return return_value
