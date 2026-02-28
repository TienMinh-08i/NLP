def count_upper_original(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    cnt = 0
    for i in range(0, len(s), 2):
        if s[i] in 'AEIOU':
            cnt += 1
    return cnt


def count_upper(s):


    return_value = count_upper_original(s)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition asserts that the returned value is equal to the count of characters in the input string 's' that are uppercase vowels and located at an even index.
    assert return_value == sum(1 for i in range(len(s)) if i % 2 == 0 and s[i] in "AEIOU")

    return return_value
