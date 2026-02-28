# The postcondition checks three properties:
# 1. The length of the returned list is the same as the input list.
# 2. Elements at odd indices in the returned list are identical to those in the input list.
# 3. The elements at even indices in the returned list, when collected, are equal to the sorted version of the collected elements at even indices from the input list.
assert (len(return_value) == len(l) and \
        all(return_value[i] == l[i] for i in range(len(l)) if i % 2 != 0) and \
        [return_value[i] for i in range(len(l)) if i % 2 == 0] == sorted([l[i] for i in range(len(l)) if i % 2 == 0]))


