```python
# This postcondition asserts that the `return_value` is a prime factor of `n`, and that no other prime number greater than `return_value` also divides `n`.
assert (n % return_value == 0 and \
        return_value > 1 and \
        all(return_value % i != 0 for i in range(2, int(return_value**0.5) + 1)) and \
        all(not (n % k == 0 and \
                 k > 1 and \
                 all(k % j != 0 for j in range(2, int(k**0.5) + 1))) \
            for k in range(return_value + 1, n + 1)))
```


