
# Response 0
# The postcondition asserts that the returned list has the same length as the input list, and each element in the returned list is the maximum value found in the corresponding prefix of the input list.
assert len(return_value) == len(numbers) and \
       all(return_value[i] == max(numbers[:i+1]) for i in range(len(numbers)))


