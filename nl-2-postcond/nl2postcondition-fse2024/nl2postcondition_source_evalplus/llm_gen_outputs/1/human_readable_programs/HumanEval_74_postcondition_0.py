# The postcondition asserts that the returned list is either the first input list (lst1) if its total character count is less than or equal to the second list's (lst2), or it is lst2 if lst1's total character count is strictly greater than lst2's.
assert (return_value == lst1 and sum(map(len, lst1)) <= sum(map(len, lst2))) or \
       (return_value == lst2 and sum(map(len, lst1)) > sum(map(len, lst2)))


