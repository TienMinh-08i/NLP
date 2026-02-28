def count_nums_original(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """

    def judge(x: int) -> int:
        l = list(str(x))
        if l[0] == '-':
            l = l[1:]
            l = list(map(int, l))
            l[0] = -l[0]
        else:
            l = list(map(int, l))
        return 1 if sum(l) > 0 else 0
    return sum(map(judge, arr))


def count_nums(arr):


    return_value = count_nums_original(arr)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition verifies that return_value matches the count of elements in arr whose signed digit sum is greater than zero, where the first digit of a negative number is treated as negative.
    assert return_value == len(list(filter(lambda x: (sum(map(int, str(x))) if x >= 0 else -int(str(x)[1]) + sum(map(int, str(x)[2:]))) > 0, arr)))
    

    return return_value
