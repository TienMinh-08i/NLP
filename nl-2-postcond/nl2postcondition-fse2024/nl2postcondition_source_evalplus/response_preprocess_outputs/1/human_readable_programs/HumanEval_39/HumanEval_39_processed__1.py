def prime_fib_original(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    import random

    def miller_rabin(n, k=10):
        """Test if n is prime using the Miller-Rabin primality test."""
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        r = 0
        d = n - 1
        while d % 2 == 0:
            r += 1
            d //= 2
        for _ in range(k):
            a = random.randint(2, n - 2)
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True
    c_prime = 0
    a, b = (0, 1)
    while c_prime < n:
        a, b = (b, a + b)
        if miller_rabin(b):
            c_prime += 1
    return b


def prime_fib(n: int):


    return_value = prime_fib_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition verifies that the returned value is a prime Fibonacci number,
    # and that it is the n-th such number in the sequence of prime Fibonacci numbers.
    # This is checked by ensuring that (n-1) prime Fibonacci numbers exist that are strictly less than the return value.
    
    # Helper function to check if a number is a perfect square.
    def _is_perfect_square(x):
        if x < 0:
            return False
        sqrt_x = int(x**0.5)
        return sqrt_x * sqrt_x == x
    
    # Helper function to check if a number is a Fibonacci number using the property
    # that a number x is Fibonacci if 5x^2 + 4 or 5x^2 - 4 is a perfect square.
    def _is_fibonacci(x):
        # 0 is technically a Fibonacci number, but the problem deals with positive primes (2, 3, 5, ...)
        # The first Fibonacci number considered by `prime_fib` for primality is 1, then 2, 3, 5, ...
        # 1 is not prime. So we check for x > 0.
        if x <= 0:
            return False
        return _is_perfect_square(5 * x * x + 4) or _is_perfect_square(5 * x * x - 4)
    
    # Helper function to check if a number is prime using trial division.
    def _is_prime(num):
        if num < 2:
            return False
        # Use all() with a generator expression for functional style
        return all(num % i != 0 for i in range(2, int(num**0.5) + 1))
    
    # Helper function to generate Fibonacci numbers up to a given limit.
    # It generates the sequence 1, 2, 3, 5, 8, ... (excluding 0).
    # This aligns with the sequence of 'b' values checked by the prime_fib function.
    def _get_fib_numbers_up_to(limit):
        fib_list = []
        a, b = 0, 1
        while b <= limit:
            fib_list.append(b)
            a, b = b, a + b
        return fib_list
    
    assert (
        # Condition 1: The return_value itself must be a Fibonacci number.
        _is_fibonacci(return_value) and
        # Condition 2: The return_value itself must be a prime number.
        _is_prime(return_value) and
        # Condition 3: There must be exactly (n - 1) prime Fibonacci numbers
        #              that are strictly less than the return_value.
        #              This ensures return_value is the n-th such number.
        len(list(filter(_is_prime, filter(_is_fibonacci, _get_fib_numbers_up_to(return_value - 1))))) == n - 1
    )

    return return_value
