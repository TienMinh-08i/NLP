```python
# The postcondition verifies that the return_value is -1 if x is greater than y or if x equals y and y is odd.
# Otherwise, if y is even and x is less than or equal to y, the return_value is y.
# If y is odd and x is less than y, the return_value is y-1.
assert return_value == (
    -1 if x > y else
    (y if y % 2 == 0 else
     (-1 if x == y else y - 1))
)
```


