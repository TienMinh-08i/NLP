def fizz_buzz_original(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    cnt = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            cnt += len(list(filter(lambda c: c == '7', str(i))))
    return cnt


def fizz_buzz(n: int):


    return_value = fizz_buzz_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition asserts that the returned value is equal to the total count of the digit '7' in all numbers less than 'n' that are divisible by 11 or 13.
    assert return_value == sum(map(lambda i: str(i).count('7'), filter(lambda i: i % 11 == 0 or i % 13 == 0, range(n))))
    

    return return_value
