def anti_shuffle_original(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    words = s.split(' ')
    return ' '.join(map(lambda x: ''.join(sorted(x, key=lambda ch: ord(ch))), words))


def anti_shuffle(s):


    return_value = anti_shuffle_original(s)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition ensures that the return value maintains the same word structure (number of words and spaces) as the input string.
    # Additionally, it verifies that each corresponding word in the return value has its characters sorted in ascending ASCII order.
    assert (lambda s_words, rv_words: len(s_words) == len(rv_words) and all("".join(sorted(s_word, key=ord)) == rv_word for s_word, rv_word in zip(s_words, rv_words)))(s.split(" "), return_value.split(" "))
    

    return return_value
