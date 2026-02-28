def triangle_area_original(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return a * h / 2


def triangle_area(a, h):


    return_value = triangle_area_original(a, h)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The return value must be exactly half the product of the side length 'a' and the height 'h'.
    assert return_value == (a * h) / 2

    return return_value
