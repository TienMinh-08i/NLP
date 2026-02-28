def check_if_last_char_is_a_letter_original(txt):
    """
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    """
    if len(txt) == 0:
        return False
    if len(txt) == 1:
        return txt.isalpha()
    return txt[-1].isalpha() and txt[-2] == ' '


def check_if_last_char_is_a_letter(txt):


    return_value = check_if_last_char_is_a_letter_original(txt)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition ensures that return_value is True if and only if the last character of the string is an alphabetical letter and it is either the only character in the string or is preceded by a space.
    assert return_value == (len(txt) > 0 and txt[-1].isalpha() and (len(txt) == 1 or txt[-2] == " "))

    return return_value
