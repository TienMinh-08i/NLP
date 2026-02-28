def next_smallest_original(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    if len(lst) <= 1:
        return None
    sorted_list = sorted(lst)
    for x in sorted_list:
        if x != sorted_list[0]:
            return x


def next_smallest(lst):


    return_value = next_smallest_original(lst)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition verifies that if the list contains one or fewer unique elements, 
    # the function returns None. Otherwise, it asserts that the return value is 
    # the second smallest unique element in the list.
    assert (len(set(lst)) <= 1 and return_value is None) or \
           (len(set(lst)) > 1 and return_value == sorted(list(set(lst)))[1])

    return return_value
