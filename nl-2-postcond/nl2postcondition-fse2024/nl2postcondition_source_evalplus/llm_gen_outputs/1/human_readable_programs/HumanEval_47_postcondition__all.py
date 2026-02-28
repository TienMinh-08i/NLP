
# Response 0
# The postcondition asserts that for a non-empty list, the return value is a median.
# This means that at least half of the elements in the input list are less than or equal to the return value,
# and at least half are greater than or equal to the return value.
# Specifically, for a list of length N, at least ceil(N/2) elements must satisfy each condition.
# ceil(N/2) can be calculated as (N + 1) // 2 for positive integers N.
assert len(l) > 0 and \
       len(list(filter(lambda x: x <= return_value, l))) >= (len(l) + 1) // 2 and \
       len(list(filter(lambda x: x >= return_value, l))) >= (len(l) + 1) // 2


