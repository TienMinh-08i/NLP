def move_one_ball_original(arr):
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:
    
    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.
                
    """
    sorted_arr = sorted(arr)
    if arr == sorted_arr:
        return True
    for i in range(1, len(arr)):
        if arr[i:] + arr[:i] == sorted_arr:
            return True
    return False


def move_one_ball(arr):


    return_value = move_one_ball_original(arr)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The return_value is True if and only if there is at most one index i where arr[i] > arr[(i + 1) % len(arr)], which is the necessary and sufficient condition for an array with unique elements to be a cyclic shift of its sorted version.
    assert return_value == (sum(1 for i in range(len(arr)) if arr[i] > arr[(i + 1) % len(arr)]) <= 1)

    return return_value
