```python
# The postcondition checks that the return value is a string,
# that it contains space-delimited numbers from 0 up to n,
# and that there are exactly n+1 such numbers, each corresponding to its index.
assert (isinstance(return_value, str) and
        len(return_value.split(' ')) == n + 1 and
        all(int(num_str) == i for i, num_str in enumerate(return_value.split(' '))))
```


