```python
# The return_value is the biggest even integer in the range [x, y] inclusive, or -1 if no such even integer exists.
assert return_value == max(list(filter(lambda n: n % 2 == 0, range(x, y + 1))) + [-1])
```


