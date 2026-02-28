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
    # The postcondition asserts that the returned value is the count of numbers in the input array
    # for which the sum of their signed digits is greater than zero.
    # For negative numbers (e.g., -123), the first digit after the sign is considered negative (-1),
    # while subsequent digits are positive (2, 3), resulting in a sum of -1 + 2 + 3 = 4.
    assert return_value == sum(
        1 for n in arr
        if sum(
            ([-int(str(n)[1])] + list(map(int, str(n)[2:]))) # For negative numbers, e.g., -123 -> -1, 2, 3
            if str(n)[0] == '-'
            else list(map(int, str(n))) # For positive numbers, e.g., 123 -> 1, 2, 3
        ) > 0
    )

    return return_value
