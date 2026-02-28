# The postcondition verifies that return_value is the total count of the digit '7' across all integers i in the range [0, n) that are divisible by either 11 or 13.
assert return_value == sum(map(lambda i: len(list(filter(lambda c: c == '7', str(i)))), filter(lambda i: i % 11 == 0 or i % 13 == 0, range(n))))


