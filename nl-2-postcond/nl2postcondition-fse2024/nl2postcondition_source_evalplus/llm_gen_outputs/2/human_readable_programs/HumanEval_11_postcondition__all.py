
# Response 0
# The postcondition verifies that return_value has the same length as input a and that each character is '1' if the corresponding characters in a and b are different, and '0' if they are the same.
assert len(return_value) == len(a) and all(res == ('1' if x != y else '0') for x, y, res in zip(a, b, return_value))


