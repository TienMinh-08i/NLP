
# Response 0
# The postcondition asserts that the function's return value is True if the product of the two fractions, when expressed as a single fraction, results in a whole number, and False otherwise.
assert return_value == ((list(map(int, x.split('/')))[0] * list(map(int, n.split('/')))[0]) % (list(map(int, x.split('/')))[1] * list(map(int, n.split('/')))[1]) == 0)


