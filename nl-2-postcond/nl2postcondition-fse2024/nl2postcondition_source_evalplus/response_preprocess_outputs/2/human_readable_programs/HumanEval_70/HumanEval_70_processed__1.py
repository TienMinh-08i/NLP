def strange_sort_list_original(lst):
    """
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    """
    sorted_list = sorted(lst)
    ans, i, j = ([], 0, len(sorted_list) - 1)
    while i < j:
        ans.append(sorted_list[i])
        ans.append(sorted_list[j])
        i += 1
        j -= 1
    if i == j:
        ans.append(sorted_list[i])
    return ans


def strange_sort_list(lst):


    return_value = strange_sort_list_original(lst)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition verifies that return_value is a permutation of the input list and that its elements follow the strange sort pattern, where even indices contain the smallest remaining values and odd indices contain the largest remaining values.
    assert len(return_value) == len(lst) and sorted(return_value) == sorted(lst) and all(return_value[i] == sorted(lst)[i // 2 if i % 2 == 0 else -1 - (i // 2)] for i in range(len(lst)))

    return return_value
