# The postcondition verifies that the `return_value` is exactly the list of positive numbers from the input list `l`, maintaining their original order.
assert return_value == list(filter(lambda x: x > 0, l))


