
# Response 0
# The postcondition verifies that the product of the prime factors in return_value is equal to n, the factors are in non-decreasing order, and each factor is a prime number.
assert __import__('math').prod(return_value) == n and return_value == sorted(return_value) and all(x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1)) for x in return_value)


