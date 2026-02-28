
# Response 0
# The postcondition ensures that return_value is the string formed by applying the swapcase method to each character in the input string and joining the results together.
assert return_value == "".join(map(lambda x: x.swapcase(), string))


