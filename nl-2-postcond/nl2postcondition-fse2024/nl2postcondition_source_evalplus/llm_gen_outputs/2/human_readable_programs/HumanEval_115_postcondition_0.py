```python
# The return_value is the total number of bucket lowerings, which is the sum of the ceiling of the number of 1s in each row (well) divided by the bucket capacity.
assert return_value == sum((sum(row) + capacity - 1) // capacity for row in grid)
```


