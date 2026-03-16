```python
# The postcondition ensures that return_value has the same length as cond and that each element return_value[i] matches the corresponding element from left_op or right_op based on the boolean value in cond[i], handling both scalar and array-like operands while treating strings and bytes as scalars.
assert len(return_value) == len(cond) and all((return_value[i] == (left_op[i] if hasattr(left_op, '__len__') and not isinstance(left_op, (str, bytes)) else left_op)) if cond[i] else (return_value[i] == (right_op[i] if hasattr(right_op, '__len__') and not isinstance(right_op, (str, bytes)) else right_op)) for i in range(len(cond)))
```


