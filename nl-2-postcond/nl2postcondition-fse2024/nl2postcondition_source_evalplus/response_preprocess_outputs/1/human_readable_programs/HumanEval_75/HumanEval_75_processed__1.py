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
    
    # The postcondition asserts that the `return_value` is true if and only if the number `a` is the product of exactly three prime numbers, counting multiplicities. It uses a recursive lambda function to find all prime factors of `a` and then checks if the count of these factors is 3.
    assert (len(
        (lambda get_factors_recursive: get_factors_recursive(get_factors_recursive, a, 2, []))(
            lambda self, n, divisor, acc_factors:
                acc_factors if n == 1
                else acc_factors + [n] if divisor * divisor > n
                else self(self, n // divisor, divisor, acc_factors + [divisor]) if n % divisor == 0
                else self(self, n, divisor + 1, acc_factors)
        )
    ) == 3) == return_value
    

    return return_value
