from typing import List

def separate_paren_groups_original(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    cnt, group, results = (0, '', [])
    for ch in paren_string:
        if ch == '(':
            cnt += 1
        if ch == ')':
            cnt -= 1
        if ch != ' ':
            group += ch
        if cnt == 0:
            if group != '':
                results.append(group)
            group = ''
    return results


def separate_paren_groups(paren_string: str) -> List[str]:


    return_value = separate_paren_groups_original(paren_string)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks two main properties:
    # 1. The concatenation of all strings in the `return_value` (which are the separated parenthesis groups) must exactly match the original `paren_string` after all spaces have been removed from it.
    # 2. Every individual string (group) in the `return_value` must be a "balanced" parenthesis string. A string is balanced if:
    #    a. The total count of opening parentheses '(' equals the total count of closing parentheses ')'.
    #    b. When scanning the string from left to right, the running count of open parentheses never drops below zero (i.e., you never encounter a closing parenthesis without a preceding opening one).
    paren_string_no_spaces = paren_string.replace(' ', '')
    # Helper lambda to check if a parenthesis string is balanced
    is_balanced = lambda s: s.count('(') == s.count(')') and min([0] + [sum(1 if c == '(' else -1 for c in s[:i+1]) for i in range(len(s))]) >= 0
    assert ''.join(return_value) == paren_string_no_spaces and \
           all(is_balanced(group) for group in return_value)
    

    return return_value
