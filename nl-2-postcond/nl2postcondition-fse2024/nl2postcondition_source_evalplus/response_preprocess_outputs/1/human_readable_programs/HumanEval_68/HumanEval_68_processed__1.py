def pluck_original(arr):
    """
    "Given an array representing a branch of a tree that has non-negative integer nodes
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [ smalest_value, its index ],
    If there are no even values or the given array is empty, return [].

    Example 1:
        Input: [4,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index.

    Example 2:
        Input: [1,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index. 

    Example 3:
        Input: []
        Output: []
    
    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]
        Explanation: 0 is the smallest value, but  there are two zeros,
                     so we will choose the first zero, which has the smallest index.

    Constraints:
        * 1 <= nodes.length <= 10000
        * 0 <= node.value
    """
    if all((val % 2 == 1 for val in arr)):
        return []
    min_even = min(filter(lambda x: x % 2 == 0, arr))
    for i in range(len(arr)):
        if arr[i] == min_even:
            return [min_even, i]


def pluck(arr):


    return_value = pluck_original(arr)
    
    # Adding imports that might be useful for postconditions
    import re 
    # This postcondition checks two main cases for the pluck function's return_value:
    # 1. If the input array `arr` is empty or contains no even numbers, the return_value must be an empty list `[]`.
    # 2. If the input array `arr` contains even numbers, the return_value must be a list `[smallest_even_value, its_smallest_index]`.
    #    - `smallest_even_value` must be an even number.
    #    - `smallest_even_value` must be the minimum among all even numbers in `arr`.
    #    - `its_smallest_index` must be the index of `smallest_even_value` in `arr`.
    #    - If `smallest_even_value` appears multiple times, `its_smallest_index` must correspond to its first occurrence (smallest index).
    assert ((len(arr) == 0 or all(x % 2 != 0 for x in arr)) and return_value == []) or \
           ((len(arr) > 0 and any(x % 2 == 0 for x in arr)) and \
            len(return_value) == 2 and \
            return_value[0] % 2 == 0 and \
            all(x >= return_value[0] for x in arr if x % 2 == 0) and \
            arr[return_value[1]] == return_value[0] and \
            all(arr[j] != return_value[0] for j in range(return_value[1])))

    return return_value
