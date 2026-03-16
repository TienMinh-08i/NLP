
# Response 0
```python
# The postcondition verifies that return_value is a boolean array with the same length as comps, where each element at index i is True if the corresponding element comps[i] matches any element in values (treating NaNs as equal and considering object identity), and False otherwise.
assert len(return_value) == len(comps) and all(res == any(c is v or (c == v) is True or (c != c and v != v) is True for v in values) for c, res in zip(comps, return_value))
```


