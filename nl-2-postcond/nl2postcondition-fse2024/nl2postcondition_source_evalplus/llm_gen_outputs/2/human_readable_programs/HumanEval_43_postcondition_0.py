# The postcondition ensures that return_value is True if and only if there are two distinct indices i and j in the list l such that the elements l[i] and l[j] sum to zero.
assert return_value == any(l[i] + l[j] == 0 for i in range(len(l)) for j in range(len(l)) if i != j)


