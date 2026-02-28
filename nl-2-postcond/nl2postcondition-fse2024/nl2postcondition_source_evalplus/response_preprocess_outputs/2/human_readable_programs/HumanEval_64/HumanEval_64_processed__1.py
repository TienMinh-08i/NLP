FIX = '\nAdd more test cases.\n'

def vowels_count_original(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    if s == '':
        return 0
    cnt = len(list(filter(lambda ch: ch in 'aeiouAEIOU', s)))
    if s[-1] in 'yY':
        cnt += 1
    return cnt


def vowels_count(s):


    return_value = vowels_count_original(s)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition verifies that return_value is the count of vowels ('a', 'e', 'i', 'o', 'u', case-insensitive) in 's', plus 1 if 's' ends with 'y' or 'Y'.
    assert return_value == len(list(filter(lambda ch: ch in 'aeiouAEIOU', s))) + (1 if s[-1:] in ('y', 'Y') else 0)

    return return_value
