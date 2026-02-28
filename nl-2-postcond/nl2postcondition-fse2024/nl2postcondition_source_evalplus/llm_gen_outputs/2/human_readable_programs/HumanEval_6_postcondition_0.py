# The return_value list must have the same number of elements as there are non-empty, space-separated groups in paren_string, and each element must equal the maximum nesting depth of parentheses within its corresponding group.
assert len(return_value) == len([g for g in paren_string.split(" ") if g != ""]) and all(v == max([g[:i+1].count("(") - g[:i+1].count(")") for i in range(len(g))] + [0]) for v, g in zip(return_value, [g for g in paren_string.split(" ") if g != ""]))


