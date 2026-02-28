def order_by_points_original(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    def weight(x):
        x_list = list(str(x))
        if x_list[0] == '-':
            x_list = x_list[1:]
            x_list = list(map(int, x_list))
            x_list[0] = -x_list[0]
        else:
            x_list = list(map(int, x_list))
        return sum(x_list)
    return sorted(nums, key=weight)


def order_by_points(nums):


    return_value = order_by_points_original(nums)
    
    # Adding imports that might be useful for postconditions
    import re 
    
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
    

    return return_value
