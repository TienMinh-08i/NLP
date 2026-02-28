```python
# The postcondition ensures that return_value is equal to the sum of all even integers located at odd indices of the list lst.
assert return_value == sum(lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0)
```


