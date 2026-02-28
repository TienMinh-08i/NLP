def is_equal_to_sum_even_original(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return n >= 8 and n % 2 == 0


def is_equal_to_sum_even(n):


    return_value = is_equal_to_sum_even_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition verifies that return_value is True if and only if n is an even integer greater than or equal to 8, which is the necessary and sufficient condition for n to be the sum of exactly four positive even numbers.
    assert return_value == (n >= 8 and n % 2 == 0)

    return return_value
