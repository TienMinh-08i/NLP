# The postcondition ensures that the function returns lst1 if its total character count is less than or equal to that of lst2, and returns lst2 otherwise.
assert return_value == (lst1 if sum(map(len, lst1)) <= sum(map(len, lst2)) else lst2)


