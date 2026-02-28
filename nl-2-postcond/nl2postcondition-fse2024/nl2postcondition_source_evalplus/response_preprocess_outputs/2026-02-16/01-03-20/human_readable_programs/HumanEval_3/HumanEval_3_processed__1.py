from typing import List

def below_zero_original(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    account = 0
    for operation in operations:
        account += operation
        if account < 0:
            return True
    return False


def below_zero(operations: List[int]) -> bool:


    return_value = below_zero_original(operations)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition asserts that the function's return value correctly indicates whether any intermediate account balance fell below zero.
    # If return_value is True, it means that at least one prefix sum of operations (representing the account balance at some point) was negative.
    # If return_value is False, it means that all prefix sums of operations were non-negative.
    assert return_value == any(map(lambda balance: balance < 0, [sum(operations[:i+1]) for i in range(len(operations))]))

    return return_value
