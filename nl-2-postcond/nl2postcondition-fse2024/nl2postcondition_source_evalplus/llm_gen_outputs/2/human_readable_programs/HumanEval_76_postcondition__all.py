
# Response 0
# The postcondition verifies that return_value is True if and only if x is equal to n raised to some non-negative integer power k.
assert return_value == any(n**k == x for k in range(len(bin(int(abs(x)))) + 2))


