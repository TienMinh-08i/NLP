def starts_one_ends_original(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    return 18 * 10 ** (n - 2)


def starts_one_ends(n):


    return_value = starts_one_ends_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition verifies that return_value matches the mathematical count of n-digit positive integers starting or ending with 1: for n=1, only '1' qualifies; for n > 1, the count is 18 * 10**(n-2).
    assert return_value == (1 if n == 1 else 18 * 10 ** (n - 2))
    

    return return_value
