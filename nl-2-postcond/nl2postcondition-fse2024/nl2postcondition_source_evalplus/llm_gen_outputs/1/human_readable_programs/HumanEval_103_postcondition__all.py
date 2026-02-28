
# Response 0
# This postcondition checks two main cases: if 'n' is greater than 'm', the return value must be -1. Otherwise, it asserts that the return value is the binary string representation of the average of 'n' and 'm', rounded to the nearest integer (using Python's default rounding rules, which round halves to the nearest even integer).
assert (n > m and return_value == -1) or \
       (n <= m and return_value == bin(round((n + m) / 2)))


