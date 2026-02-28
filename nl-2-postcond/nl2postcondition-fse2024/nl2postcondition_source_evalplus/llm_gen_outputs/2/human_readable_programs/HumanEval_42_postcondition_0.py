# The postcondition checks that the return_value list has the same length as the input list l and that each element in return_value is the corresponding element in l incremented by one.
assert len(return_value) == len(l) and all(x == y + 1 for x, y in zip(return_value, l))


