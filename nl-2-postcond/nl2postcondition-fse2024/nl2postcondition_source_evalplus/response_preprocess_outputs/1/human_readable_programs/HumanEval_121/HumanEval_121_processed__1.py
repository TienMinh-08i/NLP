def solution_original(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    return sum((lst[i] for i in range(len(lst)) if i % 2 == 0 and lst[i] % 2 == 1))


def solution(lst):


    return_value = solution_original(lst)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition asserts that the return value is equal to the sum of all elements from the input list `lst` that are located at an even index and are themselves odd.
    assert return_value == sum(element for index, element in enumerate(lst) if index % 2 == 0 and element % 2 == 1)

    return return_value
