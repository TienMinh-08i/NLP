
# Response 0
```python
# The postcondition ensures that for every index i, return_value[i] is equal to left_op[i] if cond[i] is True, and right_op[i] otherwise.
assert all(return_value[i] == (left_op[i] if cond[i] else right_op[i]) for i in range(len(cond)))
```


