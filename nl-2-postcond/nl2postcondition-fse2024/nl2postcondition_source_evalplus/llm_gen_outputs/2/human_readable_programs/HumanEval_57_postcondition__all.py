
# Response 0
```python
# The postcondition checks that return_value is True if and only if the list l is monotonically non-decreasing or non-increasing.
assert return_value == (all(l[i] <= l[i + 1] for i in range(len(l) - 1)) or all(l[i] >= l[i + 1] for i in range(len(l) - 1)))
```


