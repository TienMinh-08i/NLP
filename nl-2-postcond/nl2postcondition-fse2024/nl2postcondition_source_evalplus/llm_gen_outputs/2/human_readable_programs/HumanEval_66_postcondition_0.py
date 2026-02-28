# The postcondition verifies that the return_value is the sum of the ASCII values of all uppercase characters in the input string s.
assert return_value == sum(map(ord, filter(str.isupper, s)))


