
# Response 0
# The postcondition checks that return_value is a sorted list of all elements from x that contain only odd digits.
assert return_value == sorted(filter(lambda n: all(map(lambda d: int(d) % 2 != 0, str(n))), x))


