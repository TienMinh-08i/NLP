
# Response 0
# The return_value is the sum of the squares of all elements in lst that are positive integers and odd.
assert return_value == sum(map(lambda x: x**2, filter(lambda x: isinstance(x, int) and x > 0 and x % 2 == 1, lst)))


