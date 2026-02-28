# The postcondition asserts that the function's return value correctly indicates whether any intermediate account balance fell below zero.
# If return_value is True, it means that at least one prefix sum of operations (representing the account balance at some point) was negative.
# If return_value is False, it means that all prefix sums of operations were non-negative.
assert return_value == any(map(lambda balance: balance < 0, [sum(operations[:i+1]) for i in range(len(operations))]))


