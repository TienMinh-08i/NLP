```python
# The postcondition checks that the return value is a string consisting of space-delimited numbers,
# where the numbers are integers from 0 up to n, inclusive, in sequential order.
assert isinstance(return_value, str) and \
       len(return_value.split(' ')) == n + 1 and \
       all(int(val) == i for i, val in enumerate(return_value.split(' ')))
```


