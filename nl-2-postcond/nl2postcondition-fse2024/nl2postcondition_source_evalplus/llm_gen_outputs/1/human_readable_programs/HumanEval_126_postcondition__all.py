
# Response 0
# The postcondition asserts that the function's return value is True if and only if the input list is sorted in ascending order and no number appears more than twice in the list.
assert return_value == (
    all(lst[i] <= lst[i+1] for i in range(len(lst) - 1)) and
    all(lst.count(x) <= 2 for x in set(lst))
)


