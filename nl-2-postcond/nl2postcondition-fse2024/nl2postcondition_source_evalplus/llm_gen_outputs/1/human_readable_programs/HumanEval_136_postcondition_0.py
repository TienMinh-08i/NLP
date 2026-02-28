# The postcondition checks that the first element of the return tuple is either None (if no negative integers exist in the input list) or the largest negative integer present in the list. It also checks that the second element is either None (if no positive integers exist in the input list) or the smallest positive integer present in the list.
assert (
    (return_value[0] is None and not any(x < 0 for x in lst)) or
    (
        return_value[0] is not None and
        return_value[0] < 0 and
        return_value[0] in lst and
        all(x <= return_value[0] for x in lst if x < 0)
    )
) and (
    (return_value[1] is None and not any(x > 0 for x in lst)) or
    (
        return_value[1] is not None and
        return_value[1] > 0 and
        return_value[1] in lst and
        all(x >= return_value[1] for x in lst if x > 0)
    )
)


