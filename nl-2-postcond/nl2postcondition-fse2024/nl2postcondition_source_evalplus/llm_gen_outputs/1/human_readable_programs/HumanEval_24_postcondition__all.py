
# Response 0
```python
# The postcondition asserts that the returned value `return_value` is a divisor of `n`, is strictly smaller than `n`, and is the largest such number among all positive integers.
assert n % return_value == 0 and return_value < n and all(return_value >= k for k in filter(lambda x: n % x == 0, range(1, n)))
```


