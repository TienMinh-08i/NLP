
# Response 0
```python
# The return_value should be the sum of all elements in the first k elements of arr that have at most two digits.
assert return_value == sum(filter(lambda x: len(str(abs(x))) <= 2, arr[:k]))
```


