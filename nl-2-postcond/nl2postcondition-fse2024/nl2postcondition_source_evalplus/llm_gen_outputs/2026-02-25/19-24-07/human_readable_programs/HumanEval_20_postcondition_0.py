```python
# The postcondition asserts that the returned tuple contains two numbers from the input list,
# that the first number is less than or equal to the second, and that their difference
# is the minimum possible absolute difference between any two distinct elements (by index) in the input list.
assert (len(return_value) == 2 and
        return_value[0] in numbers and
        return_value[1] in numbers and
        return_value[0] <= return_value[1] and
        (lambda actual_diff: all(abs(numbers[i] - numbers[j]) >= actual_diff
                                 for i in range(len(numbers))
                                 for j in range(i + 1, len(numbers))))(return_value[1] - return_value[0]))
```


