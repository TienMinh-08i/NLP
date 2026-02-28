# The postcondition verifies that return_value equals x if n is prime (n >= 2 and has no divisors from 2 up to its square root) and equals y otherwise.
assert return_value == (x if (n >= 2 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))) else y)


