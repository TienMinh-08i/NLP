# The postcondition ensures that the concatenation of the strings in return_value matches the input paren_string with all spaces removed, and that each string in return_value is a non-empty, balanced parenthesis group that only reaches a balance of zero at its end.
assert "".join(return_value) == paren_string.replace(" ", "") and all(s.count('(') == s.count(')') > 0 and all(s[:i].count('(') > s[:i].count(')') for i in range(1, len(s))) for s in return_value)


