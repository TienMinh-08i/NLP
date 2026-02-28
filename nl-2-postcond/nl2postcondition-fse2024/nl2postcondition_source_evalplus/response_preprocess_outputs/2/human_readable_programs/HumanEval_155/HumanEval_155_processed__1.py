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
    # The postcondition verifies that the return value is a tuple where the first element is the count of even digits ('0', '2', '4', '6', '8') and the second element is the count of odd digits ('1', '3', '5', '7', '9') found in the string representation of the integer num.
    assert return_value == (len(list(filter(lambda ch: ch in "02468", str(num)))), len(list(filter(lambda ch: ch in "13579", str(num)))))

    return return_value
