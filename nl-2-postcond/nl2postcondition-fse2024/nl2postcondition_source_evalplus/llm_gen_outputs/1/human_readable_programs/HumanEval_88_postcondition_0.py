```
# The postcondition checks that:
# 1. If the input array is empty, the return value is an empty list.
# 2. If the input array is not empty, the return value contains the same elements as the input array,
#    just potentially in a different order (i.e., it's a permutation).
# 3. If the input array is not empty, the sorting order of the return value is determined by the parity
#    of the sum of its first and last elements:
#    - Ascending if the sum is odd.
#    - Descending if the sum is even.
#    This also covers the single-element array case, as (element + element) is always even,
#    and the descending check trivially passes for a single-element list.
assert (len(array) == 0 and return_value == []) or \
       (len(array) > 0 and \
        sorted(array) == sorted(return_value) and \
        (((array[0] + array[-1]) % 2 == 1 and all(return_value[i] <= return_value[i+1] for i in range(len(return_value) - 1))) or \
         ((array[0] + array[-1]) % 2 == 0 and all(return_value[i] >= return_value[i+1] for i in range(len(return_value) - 1)))))
```


