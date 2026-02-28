# The postcondition checks that:
# 1. The length of the returned list is identical to the input list.
# 2. Elements at indices not divisible by three in the returned list are identical to the corresponding elements in the input list.
# 3. The elements at indices divisible by three in the returned list are sorted in non-decreasing order.
# 4. The multiset of elements at indices divisible by three in the returned list is the same as the multiset of corresponding elements in the input list (i.e., they are a sorted permutation).
assert (len(l) == len(return_value) and \
        all(return_value[i] == l[i] for i in range(len(l)) if i % 3 != 0) and \
        (lambda original_thirds, returned_thirds: \
            all(returned_thirds[j] <= returned_thirds[j+1] for j in range(len(returned_thirds) - 1)) and \
            sorted(original_thirds) == sorted(returned_thirds)) \
            ([l[i] for i in range(len(l)) if i % 3 == 0], \
             [return_value[i] for i in range(len(l)) if i % 3 == 0]))


