# The postcondition states that if a valid index `k` is returned, it must be the largest index such that `arr[k]` is less than `arr[k-1]`, and all elements after `k` must be non-decreasing relative to their predecessors. If -1 is returned, it means that the entire array is non-decreasing.
assert (return_value != -1 and \
        return_value >= 1 and \
        return_value < len(arr) and \
        arr[return_value] < arr[return_value - 1] and \
        all(arr[j] >= arr[j - 1] for j in range(return_value + 1, len(arr)))) \
       or \
       (return_value == -1 and \
        all(arr[i] >= arr[i - 1] for i in range(1, len(arr))))


