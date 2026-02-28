```python
# The postcondition asserts that the `return_value` is true if and only if the number `a` is the product of exactly three prime numbers, counting multiplicities. It uses a recursive lambda function to find all prime factors of `a` and then checks if the count of these factors is 3.
assert (len(
    (lambda get_factors_recursive: get_factors_recursive(get_factors_recursive, a, 2, []))(
        lambda self, n, divisor, acc_factors:
            acc_factors if n == 1
            else acc_factors + [n] if divisor * divisor > n
            else self(self, n // divisor, divisor, acc_factors + [divisor]) if n % divisor == 0
            else self(self, n, divisor + 1, acc_factors)
    )
) == 3) == return_value
```


