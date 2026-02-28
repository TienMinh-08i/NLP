
# Response 0
```python
# The return value must have the same length as the input list, and each element must be linearly rescaled such that the minimum of the input becomes 0.0 and the maximum becomes 1.0.
assert len(return_value) == len(numbers) and all(map(lambda rv, n: abs(rv - (n - min(numbers)) / (max(numbers) - min(numbers))) < 1e-12, return_value, numbers))
```


