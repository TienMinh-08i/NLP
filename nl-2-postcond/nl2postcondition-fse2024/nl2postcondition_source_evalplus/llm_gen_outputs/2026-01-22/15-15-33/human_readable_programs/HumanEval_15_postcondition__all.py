
# Response 0
# The postcondition asserts that the return value, when split by spaces and converted to integers, forms a list of numbers identical to the sequence from 0 up to n inclusive.
assert list(map(int, return_value.split(' '))) == list(range(n + 1))


