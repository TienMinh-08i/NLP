
# Response 0
```python
# The postcondition verifies that the return value is True if and only if the square of one side length is equal to the sum of the squares of the other two side lengths.
assert return_value == (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2)
```


