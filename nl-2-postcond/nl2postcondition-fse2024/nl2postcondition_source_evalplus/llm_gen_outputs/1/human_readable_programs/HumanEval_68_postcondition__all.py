
# Response 0
# This postcondition checks two main cases for the pluck function's return_value:
# 1. If the input array `arr` is empty or contains no even numbers, the return_value must be an empty list `[]`.
# 2. If the input array `arr` contains even numbers, the return_value must be a list `[smallest_even_value, its_smallest_index]`.
#    - `smallest_even_value` must be an even number.
#    - `smallest_even_value` must be the minimum among all even numbers in `arr`.
#    - `its_smallest_index` must be the index of `smallest_even_value` in `arr`.
#    - If `smallest_even_value` appears multiple times, `its_smallest_index` must correspond to its first occurrence (smallest index).
assert ((len(arr) == 0 or all(x % 2 != 0 for x in arr)) and return_value == []) or \
       ((len(arr) > 0 and any(x % 2 == 0 for x in arr)) and \
        len(return_value) == 2 and \
        return_value[0] % 2 == 0 and \
        all(x >= return_value[0] for x in arr if x % 2 == 0) and \
        arr[return_value[1]] == return_value[0] and \
        all(arr[j] != return_value[0] for j in range(return_value[1])))


