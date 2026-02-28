
# Response 0
# The return_value must be a list containing all strings from the input list lst that have an even length, sorted primarily by their length in ascending order and secondarily by their alphabetical order.
assert return_value == sorted(filter(lambda s: len(s) % 2 == 0, lst), key=lambda s: (len(s), s))


