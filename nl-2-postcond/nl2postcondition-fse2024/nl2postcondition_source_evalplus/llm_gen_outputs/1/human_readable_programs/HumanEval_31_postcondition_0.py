# The postcondition asserts that the function's return value is True if and only if the input number n is greater than 1 and has no divisors other than 1 and itself within the range [2, n-1].
assert return_value == (n > 1 and all(n % i != 0 for i in range(2, n)))


