# The postcondition asserts that the function's return value is True if and only if there exist two distinct elements in the input list `l` that sum to zero.
assert return_value == any(l[i] + l[j] == 0 for i in range(len(l)) for j in range(len(l)) if i != j)


