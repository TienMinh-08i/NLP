
# Response 0
```python
# The return_value must be equal to the number of indices i in range(len(string)) such that the substring matches the slice of the string starting at i.
assert return_value == len(list(filter(lambda i: string[i : i + len(substring)] == substring, range(len(string)))))
```


