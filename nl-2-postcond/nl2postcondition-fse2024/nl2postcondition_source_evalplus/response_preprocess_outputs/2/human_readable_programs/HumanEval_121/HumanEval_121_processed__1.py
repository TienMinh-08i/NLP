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
    
    # The postcondition verifies that return_value is the sum of all odd integers located at even indices (0, 2, 4, ...) of the input list.
    assert return_value == sum(filter(lambda x: x % 2 == 1, lst[::2]))
    

    return return_value
