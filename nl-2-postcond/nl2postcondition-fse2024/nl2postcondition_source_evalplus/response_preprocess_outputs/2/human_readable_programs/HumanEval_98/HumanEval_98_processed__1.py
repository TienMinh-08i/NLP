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
    # The postcondition confirms that return_value is the count of uppercase vowels ('A', 'E', 'I', 'O', 'U') at even indices of the string s.
    assert return_value == len(list(filter(lambda i: s[i] in "AEIOU", range(0, len(s), 2))))

    return return_value
