from typing import List

def parse_nested_parens_original(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def count_depth(s: str) -> int:
        max_depth, cnt = (0, 0)
        for ch in s:
            if ch == '(':
                cnt += 1
            if ch == ')':
                cnt -= 1
            max_depth = max(max_depth, cnt)
        return max_depth
    return [count_depth(s) for s in paren_string.split(' ') if s != '']


def parse_nested_parens(paren_string: str) -> List[int]:


    return_value = parse_nested_parens_original(paren_string)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition asserts that the returned list of integers contains the maximum nesting depth for each group of parentheses in the input string.
    # It first splits the input string into individual parenthesis groups, filtering out any empty strings that might result from multiple spaces.
    # Then, for each such group, it functionally calculates the maximum nesting depth using `functools.reduce`.
    # The `reduce` function iterates through the characters of each group, maintaining a tuple of (maximum_depth_seen_so_far, current_depth).
    # Finally, it asserts that the `return_value` is exactly equal to the list of these calculated maximum depths.
    import functools
    
    assert return_value == list(map(lambda s: functools.reduce(lambda acc, char: (max(acc[0], acc[1] + (1 if char == '(' else -1)), acc[1] + (1 if char == '(' else -1)), s, (0, 0))[0], filter(None, paren_string.split(" "))))
    

    return return_value
