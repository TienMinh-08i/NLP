
# Response 0
# The postcondition asserts that the return value is true if and only if all three inputs are integers AND one of the numbers is equal to the sum of the other two.
assert return_value == ((type(x) is int and type(y) is int and type(z) is int) and (x == y + z or y == x + z or z == x + y))


