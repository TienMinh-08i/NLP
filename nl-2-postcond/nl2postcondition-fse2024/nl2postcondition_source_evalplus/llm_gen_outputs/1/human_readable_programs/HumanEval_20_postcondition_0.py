```python
# The postcondition checks that the returned pair (smaller, larger) is ordered correctly,
# both elements are present in the original input list, and their difference is the
# smallest possible difference between any two adjacent elements in the sorted input list.
assert (return_value[0] <= return_value[1] and
        return_value[0] in numbers and
        return_value[1] in numbers and
        (return_value[1] - return_value[0]) == min(r - l for l, r in zip(sorted(numbers)[:-1], sorted(numbers)[1:])))
```


