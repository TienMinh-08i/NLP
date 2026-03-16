```python
# The postcondition ensures that return_value contains the correct insertion indices for value in arr to maintain its 
# sorted order (as determined by the optional sorter), following the 'left' or 'right' rule: 'left' ensures 
# arr[i-1] < value <= arr[i], and 'right' ensures arr[i-1] <= value < arr[i].
assert (lambda seq, srt: all(
    0 <= i <= len(seq) and (
        (side == 'left' and (i == 0 or seq[srt[i-1] if srt is not None else i-1] < v) and (i == len(seq) or seq[srt[i] if srt is not None else i] >= v)) or
        (side == 'right' and (i == 0 or seq[srt[i-1] if srt is not None else i-1] <= v) and (i == len(seq) or seq[srt[i] if srt is not None else i] > v))
    ) for v, i in (zip(value, return_value) if hasattr(return_value, "__len__") else [(value, return_value)])
))(list(arr), list(sorter) if sorter is not None else None)
```


