# The postcondition asserts that the returned list has the same length as the input list, and for each index `i`, the element at `return_value[i]` is equal to the maximum value found in the prefix `numbers[:i+1]`.
assert len(return_value) == len(numbers) and all(return_value[i] == max(numbers[:i+1]) for i in range(len(numbers)))


