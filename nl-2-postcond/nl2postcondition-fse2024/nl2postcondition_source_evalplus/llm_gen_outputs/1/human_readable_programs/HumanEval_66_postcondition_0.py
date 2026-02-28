# The postcondition asserts that the returned value is equal to the sum of the ASCII values of all uppercase characters in the input string.
assert return_value == sum(map(ord, filter(lambda ch: ch.isupper(), s)))


