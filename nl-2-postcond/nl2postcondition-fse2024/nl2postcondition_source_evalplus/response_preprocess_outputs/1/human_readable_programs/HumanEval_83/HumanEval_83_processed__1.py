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
    # This postcondition verifies that for n=1, the count of 1-digit numbers starting or ending with 1 is 1. For n>1, it verifies that the count of n-digit positive integers that start or end with 1 is correctly calculated by the formula 18 * 10^(n-2), which accounts for numbers starting with 1, ending with 1, and subtracts the overlap of numbers starting and ending with 1.
    assert (n == 1 and return_value == 1) or (n > 1 and return_value == 18 * (10 ** (n - 2)))

    return return_value
