
# Response 0
# The postcondition asserts that the returned list contains exactly those strings from the input list that contain the given substring.
assert sorted(return_value) == sorted(list(filter(lambda s: substring in s, strings)))


