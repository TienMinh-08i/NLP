# This postcondition asserts that the return_value is the sum of elements from the first k elements of arr that have at most two digits. For negative numbers, the minus sign is not counted when determining the number of digits.
assert return_value == sum(filter(lambda x: (len(str(x)) <= 2 if x >= 0 else len(str(x)) - 1 <= 2), arr[:k]))


