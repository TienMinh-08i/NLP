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
    # This postcondition verifies that the returned list `return_value` contains the prime factors of the input `n`.
    # Specifically, it checks three conditions:
    # 1. If `n` is 1, `return_value` must be an empty list.
    # 2. If `n` is greater than 1, the product of all numbers in `return_value` must be equal to `n`.
    # 3. All numbers in `return_value` must be prime numbers (a number `f` is prime if it's greater than 1 and not divisible by any integer from 2 up to its square root).
    # 4. All numbers in `return_value` must be in non-decreasing order.
    assert (
        # Condition 1: If n is 1, the list of factors must be empty.
        (n == 1 and return_value == [])
        or
        # Condition for n > 1:
        (n > 1 and
         # Condition 2: The product of all factors must equal n.
         # math.prod is used to calculate the product of elements in a list.
         math.prod(return_value) == n and
         # Condition 3: All factors in the list must be prime numbers.
         # A number 'f' is prime if it's greater than 1 and not divisible by any integer
         # from 2 up to its square root (inclusive).
         all(
             (f > 1 and all(f % i != 0 for i in range(2, int(f**0.5) + 1)))
             for f in return_value
         ) and
         # Condition 4: The factors must be in non-decreasing order.
         # This is checked by ensuring each element is less than or equal to the next one.
         all(return_value[i] <= return_value[i+1] for i in range(len(return_value) - 1))
        )
    )

    return return_value
