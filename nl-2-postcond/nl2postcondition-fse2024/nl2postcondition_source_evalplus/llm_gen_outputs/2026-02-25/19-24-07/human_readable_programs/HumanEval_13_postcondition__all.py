
# Response 0
# The postcondition asserts that if both inputs `a` and `b` are zero, the return value is zero.
# Otherwise, it asserts that the return value is a non-zero common divisor of `a` and `b`,
# and its absolute value is greater than or equal to the absolute value of any other positive common divisor of `a` and `b`.
assert (a == 0 and b == 0 and return_value == 0) or \
       (return_value != 0 and \
        a % return_value == 0 and \
        b % return_value == 0 and \
        all(not (a % d == 0 and b % d == 0) or abs(d) <= abs(return_value) \
            for d in range(1, max(abs(a), abs(b)) + 1)))


