# The postcondition asserts that the function returns True if and only if there exists at least one point in the sequence of operations where the cumulative sum (representing the account balance) falls below zero. If no such point exists, the function must return False.
assert return_value == any(sum(operations[:i+1]) < 0 for i in range(len(operations)))


