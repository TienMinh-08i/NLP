import math

def minSubArraySum_original(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if all((x >= 0 for x in nums)):
        return min(nums)
    s, ans = (0, 0)
    for x in nums:
        s += x
        ans = min(ans, s)
        if s >= 0:
            s = 0
    return ans


def minSubArraySum(nums):


    return_value = minSubArraySum_original(nums)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    
    # This postcondition verifies that the `return_value` is indeed the minimum sum among all possible non-empty sub-arrays of `nums`. It first generates all such sub-array sums and then asserts that `return_value` is present in this list and is less than or equal to every sum in the list.
    import itertools
    assert (lambda all_subarray_sums: return_value in all_subarray_sums and all(return_value <= s for s in all_subarray_sums))(list(itertools.chain.from_iterable(map(lambda i: list(itertools.accumulate(nums[i:])), range(len(nums))))))
    

    return return_value
