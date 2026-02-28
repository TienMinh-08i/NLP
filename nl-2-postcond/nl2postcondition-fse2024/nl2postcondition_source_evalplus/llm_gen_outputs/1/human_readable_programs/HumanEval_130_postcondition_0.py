# This postcondition verifies that the returned list `return_value` has the correct length (`n + 1`) and that each element adheres to the Tribonacci sequence definition. Specifically, `return_value[0]` must be 1, `return_value[1]` must be 3, even-indexed elements `return_value[i]` (for `i >= 2`) must be `1 + i / 2`, and odd-indexed elements `return_value[i]` (for `i >= 3`) must be the sum of the two preceding elements and the value of the next element in the sequence, which for `i+1` (an even number) is `1 + (i + 1) / 2`.
assert (len(return_value) == n + 1) and \
       all(
           (i == 0 and return_value[i] == 1) or \
           (i == 1 and return_value[i] == 3) or \
           (i >= 2 and i % 2 == 0 and return_value[i] == 1 + i / 2) or \
           (i >= 2 and i % 2 != 0 and return_value[i] == return_value[i - 1] + return_value[i - 2] + (1 + (i + 1) / 2))
           for i in range(n + 1)
       )


