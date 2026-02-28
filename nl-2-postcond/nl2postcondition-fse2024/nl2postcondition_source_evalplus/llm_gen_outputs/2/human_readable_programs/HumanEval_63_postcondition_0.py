# The postcondition verifies the return_value by checking it against the n-th element of the FibFib sequence, computed using a tail-recursive lambda function that implements the recurrence relation starting from the initial values (0, 0, 1).
assert return_value == (0 if n < 2 else (lambda f, i, a, b, c: f(f, i, a, b, c))(lambda f, i, a, b, c: c if i == 2 else f(f, i - 1, b, c, a + b + c), n, 0, 0, 1))


