def can_arrange_original(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    for i in range(len(arr) - 1, 0, -1):
        if not arr[i] >= arr[i - 1]:
            return i
    return -1


def can_arrange(arr):


    return_value = can_arrange_original(arr)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition states that if a valid index `k` is returned, it must be the largest index such that `arr[k]` is less than `arr[k-1]`, and all elements after `k` must be non-decreasing relative to their predecessors. If -1 is returned, it means that the entire array is non-decreasing.
    assert (return_value != -1 and \
            return_value >= 1 and \
            return_value < len(arr) and \
            arr[return_value] < arr[return_value - 1] and \
            all(arr[j] >= arr[j - 1] for j in range(return_value + 1, len(arr)))) \
           or \
           (return_value == -1 and \
            all(arr[i] >= arr[i - 1] for i in range(1, len(arr))))

    return return_value
