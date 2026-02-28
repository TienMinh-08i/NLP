```python
# The postcondition verifies that return_value contains all strings from the input list that include the given substring, maintaining their original order.
assert return_value == list(filter(lambda s: substring in s, strings))
```


