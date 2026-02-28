def how_many_times_original(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    occurences = 0
    for i in range(len(string)):
        if string[i:].startswith(substring):
            occurences += 1
    return occurences


def how_many_times(string: str, substring: str) -> int:


    return_value = how_many_times_original(string, substring)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    
    # The postcondition asserts that if the substring is empty, the returned value is the length of the string; otherwise, it is the count of all overlapping occurrences of the substring in the string, determined using regular expression lookaheads.
    assert (return_value == len(string) if not substring else return_value == len(re.findall(f'(?={re.escape(substring)})', string)))
    

    return return_value
