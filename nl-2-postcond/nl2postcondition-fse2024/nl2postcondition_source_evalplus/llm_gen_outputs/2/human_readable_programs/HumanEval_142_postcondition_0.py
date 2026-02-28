```python
# The postcondition ensures return_value is the sum of elements from lst, where each element is squared if its index is a multiple of 3, cubed if its index is a multiple of 4 (but not 3), and kept as-is otherwise.
assert return_value == sum(num**2 if i % 3 == 0 else (num**3 if i % 4 == 0 else num) for i, num in enumerate(lst))
```


