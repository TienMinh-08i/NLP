
# Response 0
```python
# The postcondition verifies that the returned list is a permutation of the input list
# and that it is sorted according to the sum of digits, with the original index as a tie-breaker.
# For negative numbers, the sum of digits is calculated by making the first digit negative
# and summing it with the absolute values of the remaining digits (e.g., for -12, the weight is -1 + 2 = 1; for -1, the weight is -1).
# For positive numbers, it's the sum of their digits (e.g., for 12, the weight is 1 + 2 = 3).
assert (lambda weight_func:
    # 1. Check if return_value is a permutation of nums.
    #    This is done by comparing lengths and sorted versions of the lists.
    len(return_value) == len(nums)
    and sorted(return_value) == sorted(nums)
    # 2. Check if return_value matches the expected sorted order.
    #    We create a list of (original_index, value) tuples from nums,
    #    sort them using the weight_func as the primary key and original_index as the secondary key,
    #    and then extract the values to form the expected sorted list.
    and return_value == list(map(lambda item: item[1],
        sorted(
            list(enumerate(nums)),  # Pair each number with its original index
            key=lambda item: (weight_func(item[1]), item[0]) # Sort by weight, then by original index
        )
    ))
)(
    # Define the weight function for postcondition evaluation.
    # This lambda replicates the logic of the `weight` function inside `order_by_points`.
    lambda x: (
        (lambda s:
            # Handle negative numbers with multiple digits (e.g., -12 -> -1 + 2 = 1)
            (-int(s[1]) + sum(map(int, s[2:]))) if s.startswith('-') and len(s) > 2 else
            # Handle negative numbers with a single digit (e.g., -1 -> -1)
            (-int(s[1])) if s.startswith('-') and len(s) == 2 else
            # Handle positive numbers (e.g., 12 -> 1 + 2 = 3)
            sum(map(int, s))
        )(str(x)) # Convert the number to string to process its digits
    )
)
```


