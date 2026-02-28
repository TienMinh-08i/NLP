# The postcondition verifies that return_value is 'Yes' if and only if either concatenation of the two strings in lst (lst[0]+lst[1] or lst[1]+lst[0]) results in a balanced parentheses string, where balance is defined as having an equal total number of open and close parentheses and no prefix having more close than open parentheses.
assert return_value == ('Yes' if any(s.count('(') == s.count(')') and all(s[:i].count('(') >= s[:i].count(')') for i in range(len(s) + 1)) for s in [lst[0] + lst[1], lst[1] + lst[0]]) else 'No')


