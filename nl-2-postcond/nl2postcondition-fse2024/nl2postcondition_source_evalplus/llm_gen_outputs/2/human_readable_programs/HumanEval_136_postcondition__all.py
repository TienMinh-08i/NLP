
# Response 0
```python
# The postcondition verifies that return_value is a tuple where the first element is the largest negative integer in lst and the second is the smallest positive integer, using None for either if no such integers exist.
assert return_value == (max(filter(lambda x: x < 0, lst)) if any(map(lambda x: x < 0, lst)) else None, min(filter(lambda x: x > 0, lst)) if any(map(lambda x: x > 0, lst)) else None)
```


