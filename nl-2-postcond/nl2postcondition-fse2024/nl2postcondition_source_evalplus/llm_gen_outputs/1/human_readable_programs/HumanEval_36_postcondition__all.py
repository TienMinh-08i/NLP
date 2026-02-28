
# Response 0
```python
# The postcondition asserts that the returned value is equal to the total count of the digit '7' in all numbers less than 'n' that are divisible by 11 or 13.
assert return_value == sum(map(lambda i: str(i).count('7'), filter(lambda i: i % 11 == 0 or i % 13 == 0, range(n))))
```


