def add_original(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    s = 0
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            s += lst[i]
    return s


def add(lst):


    return_value = add_original(lst)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition asserts that the `return_value` is equal to the sum of all elements `value` from the input list `lst` where `value` is at an odd `index` and `value` itself is even.
    assert return_value == sum(map(lambda item: item[1], filter(lambda item: item[0] % 2 != 0 and item[1] % 2 == 0, enumerate(lst))))

    return return_value
