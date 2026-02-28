
# Response 0
# The postcondition verifies that the length of the returned list of coefficients is correct (one less than the input list, or zero if the input was empty or a constant), and that each coefficient in the returned list is the product of the corresponding original coefficient and its original power.
assert len(return_value) == max(0, len(xs) - 1) and all(return_value[j] == xs[j+1] * (j+1) for j in range(len(return_value)))


