```python
# The return_value is True if and only if every character in s0 is present in s1 and every character in s1 is present in s0.
assert return_value == (all(map(lambda c: c in s1, s0)) and all(map(lambda c: c in s0, s1)))
```


