
# Response 0
# The postcondition asserts that return_value is True if and only if n is an integer greater than 1 that has no divisors in the range [2, n-1].
assert return_value == (n > 1 and all(n % i != 0 for i in range(2, n)))


