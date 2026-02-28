# The postcondition asserts that the `return_value` is a list containing only integers, and that it is exactly the sequence of integer elements found in the `values` input list, preserving their original order.
assert return_value == list(filter(lambda x: type(x) == int, values))


