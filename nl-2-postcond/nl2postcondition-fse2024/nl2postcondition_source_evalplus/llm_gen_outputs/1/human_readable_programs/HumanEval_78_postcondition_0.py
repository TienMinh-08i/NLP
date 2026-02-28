# The postcondition asserts that the returned value is equal to the count of characters in the input hexadecimal string that are among the prime hexadecimal digits (2, 3, 5, 7, B, D).
assert len(list(filter(lambda x: x in "2357BD", num))) == return_value


