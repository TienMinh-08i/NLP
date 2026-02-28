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
    # The postcondition asserts that the return_value correctly reflects the branching logic of the split_words function.
    # If the input text contains any whitespace, the return_value must be the list of words split by whitespace.
    # Otherwise, if the input text contains a comma, the return_value must be the list of words split by commas.
    # Otherwise (no whitespace and no commas), the return_value must be the count of lowercase letters in the text
    # whose alphabetical order (0-indexed from 'a') is odd.
    assert (any(ws_char in txt for ws_char in ' \n\r\t') and return_value == txt.split()) or \
           (not any(ws_char in txt for ws_char in ' \n\r\t') and ',' in txt and return_value == txt.split(',')) or \
           (not any(ws_char in txt for ws_char in ' \n\r\t') and ',' not in txt and return_value == sum(1 for ch in txt if ch.islower() and (ord(ch) - ord('a')) % 2 == 1))

    return return_value
