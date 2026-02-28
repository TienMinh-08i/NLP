
# Response 0
```python
# The postcondition verifies that return_value matches the mathematical count of n-digit positive integers starting or ending with 1: for n=1, only '1' qualifies; for n > 1, the count is 18 * 10**(n-2).
assert return_value == (1 if n == 1 else 18 * 10 ** (n - 2))
```


