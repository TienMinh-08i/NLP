
# Response 0
```python
# The postcondition verifies that return_value is True if and only if x, y, and z are all integers and one of the values is the sum of the other two.
assert return_value == (all(type(val) == int for val in [x, y, z]) and any([x == y + z, y == x + z, z == y + x]))
```


