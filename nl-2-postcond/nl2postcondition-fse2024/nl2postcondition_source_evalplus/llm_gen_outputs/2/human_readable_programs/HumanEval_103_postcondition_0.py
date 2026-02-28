# The postcondition verifies that if n is greater than m, the return value is -1; otherwise, it is the binary representation of the average of n and m rounded to the nearest integer.
assert return_value == (-1 if n > m else bin(round((n + m) / 2)))


