def correct_bracketing_original(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    cnt = 0
    for x in brackets:
        if x == '<':
            cnt += 1
        if x == '>':
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0


def correct_bracketing(brackets: str):


    return_value = correct_bracketing_original(brackets)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The return_value is True if and only if the total number of opening brackets '<' matches the total number of closing brackets '>' and for every prefix of the input string, the number of opening brackets is at least the number of closing brackets.
    assert return_value == (brackets.count("<") == brackets.count(">") and all(brackets[:i].count("<") >= brackets[:i].count(">") for i in range(len(brackets) + 1)))
    

    return return_value
