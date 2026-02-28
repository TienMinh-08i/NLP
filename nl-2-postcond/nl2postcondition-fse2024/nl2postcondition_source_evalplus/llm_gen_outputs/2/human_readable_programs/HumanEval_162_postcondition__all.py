
# Response 0
# The postcondition verifies that if the input string is empty, the function returns None; otherwise, it returns a 32-character lowercase hexadecimal string.
assert (return_value is None if text == "" else (isinstance(return_value, str) and len(return_value) == 32 and all(c in '0123456789abcdef' for c in return_value)))


