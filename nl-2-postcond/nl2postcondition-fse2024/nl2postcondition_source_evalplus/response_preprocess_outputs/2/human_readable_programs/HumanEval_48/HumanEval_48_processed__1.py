def is_palindrome_original(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    return text == text[::-1]


def is_palindrome(text: str):


    return_value = is_palindrome_original(text)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition verifies that return_value is True if and only if every character in the string text matches the character at the corresponding position from the end.
    assert return_value == all(text[i] == text[len(text) - 1 - i] for i in range(len(text)))

    return return_value
