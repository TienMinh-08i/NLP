# The postcondition asserts that the function returns True if and only if
# all prefix sums of bracket values (where '(' is +1 and ')' is -1) are non-negative,
# and the total sum of bracket values for the entire string is zero.
# Otherwise, the function returns False.
assert return_value == (
    all(sum(1 if c == '(' else -1 for c in brackets[:i]) >= 0 for i in range(len(brackets) + 1))
    and
    sum(1 if c == '(' else -1 for c in brackets) == 0
)


