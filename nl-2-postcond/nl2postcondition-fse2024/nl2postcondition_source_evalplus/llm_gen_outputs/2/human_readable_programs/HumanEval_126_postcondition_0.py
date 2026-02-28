# The postcondition checks that return_value is True if and only if the list is sorted in non-decreasing order and no element appears more than twice.
assert return_value == (lst == sorted(lst) and all(lst.count(x) <= 2 for x in lst))


