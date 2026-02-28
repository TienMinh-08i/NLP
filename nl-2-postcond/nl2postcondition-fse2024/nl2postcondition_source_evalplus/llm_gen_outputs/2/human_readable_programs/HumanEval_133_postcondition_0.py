# The return_value is the sum of the squares of the ceiling of each number in the input list.
assert return_value == sum(map(lambda x: (int(x) + (1 if x > int(x) else 0))**2, lst))


