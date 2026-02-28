# Each element in the return_value must be the maximum value found in the numbers list from its beginning up to the current index, and both lists must have the same length.
assert len(return_value) == len(numbers) and all(return_value[i] == max(numbers[:(i+1)]) for i in range(len(numbers)))


