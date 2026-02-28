
# Response 0
# The postcondition asserts two main properties of the return value:
# 1. Correctness and Completeness: The set of (row, column) tuples in the return_value
#    must exactly match the set of all occurrences of 'x' within the input 'lst'.
# 2. Sorting: The return_value must be sorted such that tuples are ordered by
#    row in ascending order, and for tuples within the same row, by column in
#    descending order.
assert (set(return_value) == set([(r, c) for r, row in enumerate(lst) for c, val in enumerate(row) if val == x])) and \
       all((return_value[i][0] < return_value[i+1][0]) or \
           (return_value[i][0] == return_value[i+1][0] and return_value[i][1] > return_value[i+1][1]) \
           for i in range(len(return_value) - 1))


