```python
# The postcondition ensures that return_value is the list of all prime numbers strictly less than n, in ascending order.
assert return_value == [x for x in range(2, n) if all(x % i != 0 for i in range(2, x))]
```


