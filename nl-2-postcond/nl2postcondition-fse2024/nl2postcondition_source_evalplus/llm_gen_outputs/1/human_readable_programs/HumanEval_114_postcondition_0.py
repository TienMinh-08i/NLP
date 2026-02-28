```
# This postcondition verifies that the `return_value` is indeed the minimum sum among all possible non-empty sub-arrays of `nums`. It first generates all such sub-array sums and then asserts that `return_value` is present in this list and is less than or equal to every sum in the list.
import itertools
assert (lambda all_subarray_sums: return_value in all_subarray_sums and all(return_value <= s for s in all_subarray_sums))(list(itertools.chain.from_iterable(map(lambda i: list(itertools.accumulate(nums[i:])), range(len(nums))))))
```


