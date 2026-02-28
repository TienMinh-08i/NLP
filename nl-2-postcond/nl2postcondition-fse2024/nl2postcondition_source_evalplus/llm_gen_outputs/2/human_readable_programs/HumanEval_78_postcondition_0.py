```python
# The postcondition checks that the return_value correctly counts the occurrences of the prime hexadecimal digits '2', '3', '5', '7', 'B', and 'D' within the input string num.
assert return_value == len(list(filter(lambda x: x in "2357BD", num)))
```


