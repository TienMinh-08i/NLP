```python
# The postcondition asserts that the returned list `return_value` contains exactly all prime numbers that are strictly less than the input `n`, in ascending order.
assert (lambda n_val, ret_val:
    # Define a helper lambda function `is_prime` to check if a number is prime.
    # A number `num` is prime if it's greater than 1 and not divisible by any integer
    # from 2 up to its square root.
    (lambda is_prime:
        # The `return_value` must be identical to a list constructed by iterating
        # through numbers from 2 up to (but not including) `n_val`,
        # and including only those numbers for which `is_prime` returns True.
        ret_val == [i for i in range(2, n_val) if is_prime(i)]
    )(lambda num: num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)))
)(n, return_value)
```


