def iscube_original(a):
    """
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    """
    a = abs(a)
    return int(round(a ** (1.0 / 3))) ** 3 == a


def iscube(a):


    return_value = iscube_original(a)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition checks that the return_value is True if and only if there exists an integer i in the range [-abs(a), abs(a)] such that i cubed is equal to the input integer a.
    assert return_value == any(i**3 == a for i in range(-abs(a), abs(a) + 1))

    return return_value
