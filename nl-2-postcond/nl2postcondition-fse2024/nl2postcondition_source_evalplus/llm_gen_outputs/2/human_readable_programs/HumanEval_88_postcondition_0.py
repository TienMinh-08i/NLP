```python
# The postcondition ensures that return_value is a permutation of the input array, sorted in ascending order if the sum of the first and last elements is odd, and in descending order if the sum is even.
assert sorted(return_value) == sorted(array) and (len(array) == 0 or return_value == sorted(array, reverse=((array[0] + array[-1]) % 2 == 0)))
```


