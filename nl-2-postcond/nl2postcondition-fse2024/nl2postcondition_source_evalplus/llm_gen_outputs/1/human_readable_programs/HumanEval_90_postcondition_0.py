# The postcondition verifies that if the list contains one or fewer unique elements, 
# the function returns None. Otherwise, it asserts that the return value is 
# the second smallest unique element in the list.
assert (len(set(lst)) <= 1 and return_value is None) or \
       (len(set(lst)) > 1 and return_value == sorted(list(set(lst)))[1])


