```python
# The return_value is True if and only if key is in cat.categories and its location in categories (or at least one of its locations if it's an iterable like a numpy array) is present in the container.
assert return_value == any((any(loc_ in container for loc_ in loc) if hasattr(loc, '__iter__') else loc in container) for loc in ([cat.categories.get_loc(key)] if key in cat.categories else []))
```


