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
    # This postcondition asserts that the returned value is equal to the sum of the count of standard vowels ('a', 'e', 'i', 'o', 'u', case-insensitive) in the input string and an additional 1 if the last character of the string is 'y' (case-insensitive), otherwise 0.
    assert return_value == len(list(filter(lambda char: char.lower() in "aeiou", s))) + (1 if s and s[-1].lower() == 'y' else 0)

    return return_value
