```python
# The postcondition verifies that all digits in the string return_value are less than the base and that the base-base representation correctly sums to the original integer x.
assert all(int(d) < base for d in return_value) and sum(int(return_value[i]) * (base ** (len(return_value) - 1 - i)) for i in range(len(return_value))) == x
```


