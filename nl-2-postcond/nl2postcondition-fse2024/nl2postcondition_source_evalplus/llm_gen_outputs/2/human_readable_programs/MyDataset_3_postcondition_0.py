# The postcondition verifies that for each value and its corresponding returned index i, the elements of the sorted array (optionally ordered by sorter) are correctly partitioned: for 'left', elements before i are less than the value and elements from i onwards are greater than or equal to the value; for 'right', elements before i are less than or equal to the value and elements from i onwards are greater than the value.
assert all(
    (
        all((arr.iloc if hasattr(arr, 'iloc') else arr)[sorter[j] if sorter is not None else j] < v for j in range(i)) and
        all((arr.iloc if hasattr(arr, 'iloc') else arr)[sorter[j] if sorter is not None else j] >= v for j in range(i, len(arr)))
    ) if side == 'left' else (
        all((arr.iloc if hasattr(arr, 'iloc') else arr)[sorter[j] if sorter is not None else j] <= v for j in range(i)) and
        all((arr.iloc if hasattr(arr, 'iloc') else arr)[sorter[j] if sorter is not None else j] > v for j in range(i, len(arr)))
    )
    for v, i in (zip(value, return_value) if hasattr(return_value, '__iter__') else [(value, return_value)])
)


