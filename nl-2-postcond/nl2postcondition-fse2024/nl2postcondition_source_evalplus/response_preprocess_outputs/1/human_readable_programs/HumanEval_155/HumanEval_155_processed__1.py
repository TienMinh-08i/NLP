def even_odd_count_original(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even, odd = (0, 0)
    for ch in str(num):
        if ch in '02468':
            even += 1
        if ch in '13579':
            odd += 1
    return (even, odd)


def even_odd_count(num):


    return_value = even_odd_count_original(num)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition asserts that the first element of the return value equals the count of even digits in the input number, and the second element equals the count of odd digits in the input number.
    assert (sum(1 for digit in str(num) if digit in "02468") == return_value[0] and
            sum(1 for digit in str(num) if digit in "13579") == return_value[1])
    

    return return_value
