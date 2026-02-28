def remove_vowels_original(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef
ghijklm")
    'bcdf
ghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    return ''.join(list(filter(lambda ch: ch not in 'aeiouAEIOU', text)))


def remove_vowels(text):


    return_value = remove_vowels_original(text)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition asserts that the returned string is exactly what is obtained by filtering out all vowels (case-insensitive) from the input string, thus ensuring all non-vowel characters are preserved in order and no vowels are present.
    assert return_value == "".join(filter(lambda ch: ch not in "aeiouAEIOU", text))

    return return_value
