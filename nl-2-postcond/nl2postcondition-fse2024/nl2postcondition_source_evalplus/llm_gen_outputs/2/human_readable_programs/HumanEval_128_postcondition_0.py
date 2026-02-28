# The postcondition ensures that the return value is None if the input array is empty, 0 if the array contains at least one zero, and otherwise equals the sum of the absolute values of the elements multiplied by the product of their signs (1 if the count of negative elements is even, and -1 if it is odd).
assert return_value == (None if len(arr) == 0 else (0 if 0 in arr else sum(map(abs, arr)) * ((-1) ** len(list(filter(lambda x: x < 0, arr))))))


