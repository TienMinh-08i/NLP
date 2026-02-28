def split_words_original(txt):
    """
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    """
    whitespace = tuple(' \n\r\t')
    if any([x in txt for x in whitespace]):
        return txt.split()
    if ',' in txt:
        return txt.split(',')
    cnt = 0
    for ch in txt:
        if ch.islower() and (ord(ch) - ord('a')) % 2 == 1:
            cnt += 1
    return cnt


def split_words(txt):


    return_value = split_words_original(txt)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition verifies that return_value is the result of txt.split() if whitespace is present, 
    # txt.split(',') if no whitespace but a comma is present, or the count of lowercase letters 
    # with an odd alphabetical index (a=0, b=1, ...) if neither exists.
    assert (return_value == txt.split()) if any(x in txt for x in ' \n\r\t') else (return_value == txt.split(',') if ',' in txt else return_value == sum(1 for ch in txt if ch.islower() and (ord(ch) - ord('a')) % 2 == 1))
    

    return return_value
