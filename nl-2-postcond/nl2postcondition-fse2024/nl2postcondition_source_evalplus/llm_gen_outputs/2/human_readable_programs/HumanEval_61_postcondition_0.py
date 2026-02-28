# The postcondition verifies that return_value is True if and only if the string contains an equal number of opening and closing brackets and, for every prefix of the string, the number of opening brackets is at least the number of closing brackets.
assert return_value == (brackets.count('(') == brackets.count(')') and all(brackets[:i].count('(') >= brackets[:i].count(')') for i in range(len(brackets) + 1)))


