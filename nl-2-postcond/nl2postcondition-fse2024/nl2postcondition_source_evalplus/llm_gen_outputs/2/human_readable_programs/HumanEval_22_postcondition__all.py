
# Response 0
# The postcondition ensures that return_value is a list containing only the items from the input list 'values' that are of type int, in their original order.
assert return_value == list(filter(lambda x: type(x) == int, values))


