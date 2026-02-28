
# Response 0
# This postcondition asserts that the returned list contains exactly the strings from the input list that include the given substring, maintaining their original relative order.
assert return_value == list(filter(lambda s: substring in s, strings))


