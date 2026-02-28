# This postcondition asserts that the function's return value is true if and only if any of the cumulative sums of the operations results in a balance less than zero. Otherwise, the return value must be false, indicating that the balance never dropped below zero.
assert return_value == any(sum(operations[:i+1]) < 0 for i in range(len(operations)))


