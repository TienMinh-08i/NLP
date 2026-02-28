def digits_original(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    has_odd, prod = (False, 1)
    for ch in str(n):
        if int(ch) % 2 == 1:
            has_odd = True
            prod *= int(ch)
    return 0 if not has_odd else prod


def digits(n):


    return_value = digits_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition verifies that return_value is 0 if n contains no odd digits, and otherwise equals the product of all its odd digits.
    assert return_value == (0 if not __import__('re').findall('[13579]', str(n)) else __import__('math').prod(map(int, __import__('re').findall('[13579]', str(n)))))
    

    return return_value
