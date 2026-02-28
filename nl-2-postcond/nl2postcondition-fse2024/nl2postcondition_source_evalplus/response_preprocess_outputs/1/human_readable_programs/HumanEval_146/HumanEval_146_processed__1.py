def specialFilter_original(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    ans, odd = (0, ['1', '3', '5', '7', '9'])
    for num in nums:
        if num > 10 and str(num)[0] in odd and (str(num)[-1] in odd):
            ans += 1
    return ans


def specialFilter(nums):


    return_value = specialFilter_original(nums)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition asserts that the return_value is equal to the count of numbers in the input array 'nums' that are greater than 10 and have both their first and last digits as odd numbers (1, 3, 5, 7, 9).
    assert return_value == len(list(filter(lambda num: num > 10 and str(num)[0] in ["1", "3", "5", "7", "9"] and str(num)[-1] in ["1", "3", "5", "7", "9"], nums)))

    return return_value
