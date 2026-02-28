
# Response 0
# The postcondition asserts that the function's return value is True if and only if the input list is either entirely non-decreasing or entirely non-increasing.
assert return_value == (all(l[i] <= l[i+1] for i in range(len(l) - 1)) or all(l[i] >= l[i+1] for i in range(len(l) - 1)))


