
# Response 0
# The return_value is a common divisor of a and b, and no integer with an absolute value greater than that of return_value is a common divisor of both a and b.
assert (a == 0 and b == 0 and return_value == 0) or ((a != 0 or b != 0) and return_value != 0 and a % return_value == 0 and b % return_value == 0 and all(a % i != 0 or b % i != 0 for i in range(abs(return_value) + 1, max(abs(a), abs(b)) + 1)))


