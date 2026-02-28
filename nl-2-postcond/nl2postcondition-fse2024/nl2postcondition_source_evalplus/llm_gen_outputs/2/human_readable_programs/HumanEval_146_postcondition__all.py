
# Response 0
# The return_value should be the number of elements in nums that are greater than 10 and have an odd digit (1, 3, 5, 7, 9) as both their first and last digit.
assert return_value == len([num for num in nums if num > 10 and str(num)[0] in '13579' and str(num)[-1] in '13579'])


