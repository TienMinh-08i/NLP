def choose_num_original(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        return -1
    if x == y:
        return y if y % 2 == 0 else -1
    return y if y % 2 == 0 else y - 1


def choose_num(x, y):


    return_value = choose_num_original(x, y)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition verifies that the return_value is -1 if x is greater than y or if x equals y and y is odd.
    # Otherwise, if y is even and x is less than or equal to y, the return_value is y.
    # If y is odd and x is less than y, the return_value is y-1.
    assert return_value == (
        -1 if x > y else
        (y if y % 2 == 0 else
         (-1 if x == y else y - 1))
    )
    

    return return_value
