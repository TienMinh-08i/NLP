```python
# The postcondition ensures that return_value is the string in words with the maximum number of unique characters (with lexicographical priority for ties), or an empty string if words is empty.
assert (return_value == "" if not words else (return_value in words and all(len(set(return_value)) > len(set(w)) or (len(set(return_value)) == len(set(w)) and return_value <= w) for w in words)))
```


