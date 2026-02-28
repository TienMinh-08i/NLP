# The postcondition asserts that the `return_value` is equal to the number of unique characters in the input `string` after converting all characters to lowercase.
assert return_value == len(set(string.lower()))


