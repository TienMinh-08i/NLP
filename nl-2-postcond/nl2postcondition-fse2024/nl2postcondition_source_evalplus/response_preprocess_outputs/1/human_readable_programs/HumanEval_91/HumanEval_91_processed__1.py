def is_bored_original(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    sentences = map(lambda x: x.strip(), S.replace('?', '.').replace('!', '.').split('.'))
    return len([s for s in sentences if s.startswith('I ')])


def is_bored(S):


    return_value = is_bored_original(S)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition asserts that the return_value is equal to the count of sentences in the input string S that start with "I " (case-sensitive).
    # Sentences are identified by first replacing '?' and '!' with '.', then splitting the string by '.', and finally stripping leading/trailing whitespace from each segment.
    assert return_value == len(list(filter(lambda s: s.startswith("I "), map(lambda x: x.strip(), S.replace("?", ".").replace("!", ".").split(".")))))

    return return_value
