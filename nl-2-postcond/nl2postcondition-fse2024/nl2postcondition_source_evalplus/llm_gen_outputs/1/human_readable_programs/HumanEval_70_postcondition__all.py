
# Response 0
# The postcondition checks that the length of the returned list is the same as the input list,
# that the returned list contains the same elements as the input list (just reordered),
# and that the elements follow the strange sorting pattern: minimum, then maximum of remaining,
# then second minimum, then second maximum of remaining, and so on.
s_lst = sorted(lst)
assert (len(return_value) == len(lst) and
        s_lst == sorted(return_value) and
        (len(lst) == 0 or
         all( (return_value[k] == s_lst[k // 2] if k % 2 == 0 else
               return_value[k] == s_lst[len(lst) - 1 - (k - 1) // 2])
              for k in range(len(lst)) )))


