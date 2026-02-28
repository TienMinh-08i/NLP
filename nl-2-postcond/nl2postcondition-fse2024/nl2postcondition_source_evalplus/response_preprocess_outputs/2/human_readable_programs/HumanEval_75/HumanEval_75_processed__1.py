def is_multiply_prime_original(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a <= 1:
        return False
    isprime = [True] * (a + 1)
    for i in range(2, a + 1):
        if isprime[i]:
            for j in range(i + i, a + 1, i):
                isprime[j] = False
    cnt, tmp = (0, a)
    for i in range(2, a + 1):
        while isprime[i] and tmp % i == 0:
            tmp //= i
            cnt += 1
    return cnt == 3


def is_multiply_prime(a):


    return_value = is_multiply_prime_original(a)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition verifies that return_value is True if and only if a can be expressed as the product of three prime numbers, where each prime is an integer greater than 1 with no divisors other than 1 and itself.
    assert return_value == any(p1 * p2 * p3 == a for p1 in range(2, a + 1) if all(p1 % i != 0 for i in range(2, p1)) for p2 in range(2, a + 1) if all(p2 % i != 0 for i in range(2, p2)) for p3 in range(2, a + 1) if all(p3 % i != 0 for i in range(2, p3)))
    

    return return_value
