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
    # The postcondition ensures that the concatenation of the strings in return_value matches the input paren_string with all spaces removed, and that each string in return_value is a non-empty, balanced parenthesis group that only reaches a balance of zero at its end.
    assert "".join(return_value) == paren_string.replace(" ", "") and all(s.count('(') == s.count(')') > 0 and all(s[:i].count('(') > s[:i].count(')') for i in range(1, len(s))) for s in return_value)

    return return_value
