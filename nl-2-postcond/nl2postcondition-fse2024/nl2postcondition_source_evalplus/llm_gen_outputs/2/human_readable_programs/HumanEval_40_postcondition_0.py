# The postcondition asserts that return_value is True if and only if there exist three distinct indices i, j, and k in the input list l such that the sum of the elements at those indices is zero.
assert return_value == any(l[i] + l[j] + l[k] == 0 for i in range(len(l)) for j in range(i + 1, len(l)) for k in range(j + 1, len(l)))


