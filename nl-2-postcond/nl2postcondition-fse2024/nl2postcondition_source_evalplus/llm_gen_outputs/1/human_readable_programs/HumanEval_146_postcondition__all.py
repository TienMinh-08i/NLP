
# Response 0
# The postcondition asserts that the return_value is equal to the count of numbers in the input array 'nums' that are greater than 10 and have both their first and last digits as odd numbers (1, 3, 5, 7, 9).
assert return_value == len(list(filter(lambda num: num > 10 and str(num)[0] in ["1", "3", "5", "7", "9"] and str(num)[-1] in ["1", "3", "5", "7", "9"], nums)))


