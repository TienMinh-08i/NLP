```python
# The postcondition asserts that the return_value is exactly the list of strings from the input 'strings' that begin with the specified 'prefix', maintaining their original order.
assert return_value == list(filter(lambda s: s.startswith(prefix), strings))
```


