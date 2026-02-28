def generate_integers_original(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        a, b = (b, a)
    return [i for i in range(a, min(b + 1, 10)) if i % 2 == 0]


def generate_integers(a, b):


    return_value = generate_integers_original(a, b)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The return_value is equal to the list of all even digits that fall within the range [min(a, b), max(a, b)], sorted in ascending order.
    assert return_value == list(filter(lambda x: x % 2 == 0, range(min(a, b), min(max(a, b) + 1, 10))))

    return return_value
