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
    
    # The postcondition asserts that the returned list consists of non-empty, balanced parenthesis strings,
    # and that concatenating these strings results in the original input string with all spaces removed.
    assert (
        all(
            # Each group must be non-empty
            len(group) > 0
            and
            # Each group must only contain parentheses characters
            all(c in '()' for c in group)
            and
            # Each group must have an equal number of opening and closing parentheses
            group.count('(') == group.count(')')
            and
            # The running balance of parentheses (count of '(' minus count of ')') must never be negative
            # when traversing the group from left to right, and must end at zero.
            # The 'group.count('(') == group.count(')')' condition ensures it ends at zero.
            all(
                sum(1 if char == '(' else -1 for char in group[:idx+1]) >= 0
                for idx in range(len(group))
            )
            for group in return_value
        )
        and
        # The concatenation of all groups in the return_value must be exactly equal
        # to the original input string after all spaces have been removed.
        "".join(return_value) == paren_string.replace(" ", "")
    )
    

    return return_value
