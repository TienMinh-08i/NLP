# The postcondition asserts that the function returns "YES" if and only if the number of odd elements in lst1 is less than or equal to the number of even elements in lst2.
assert (return_value == "YES") == (len(list(filter(lambda x: x % 2 != 0, lst1))) <= len(list(filter(lambda x: x % 2 == 0, lst2))))


