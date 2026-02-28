```
# The postcondition verifies that the returned value matches the n-th element of the Fib4 sequence.
# It computes the sequence iteratively up to n by encapsulating the stateful generation within nested lambdas,
# using the `map` function to apply a side-effecting lambda that appends new Fib4 numbers to a list,
# and then extracts the n-th element from the generated list. This approach handles all non-negative n.
assert (lambda n_val: \
            # This inner lambda initializes the base sequence values [fib4(0), fib4(1), fib4(2), fib4(3)].
            # This list will be mutated by the map function to extend the sequence.
            (lambda fibs_list: \
                # The 'list(...)' call forces the evaluation of the map object, which in turn executes
                # the inner lambda for each 'i' in the range. The inner lambda's side effect is to
                # append the next Fib4 number to 'fibs_list'.
                # The outer tuple ensures that both the side effect (list population) happens
                # and the final desired value (fibs_list[n_val]) is available for selection.
                (list(map(lambda i: fibs_list.append(sum(fibs_list[i-4:i])), range(4, n_val + 1))), \
                 fibs_list[n_val]) \
            )([0, 0, 2, 0]) \
        )[1])(n) == return_value
```


