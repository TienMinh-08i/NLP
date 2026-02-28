def any_int_original(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  

    
    """
    if type(x) != int or type(y) != int or type(z) != int:
        return False
    return x == y + z or y == x + z or z == y + x


def any_int(x, y, z):


    return_value = any_int_original(x, y, z)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition verifies that return_value is True if and only if x, y, and z are all integers and one of the values is the sum of the other two.
    assert return_value == (all(type(val) == int for val in [x, y, z]) and any([x == y + z, y == x + z, z == y + x]))
    

    return return_value
