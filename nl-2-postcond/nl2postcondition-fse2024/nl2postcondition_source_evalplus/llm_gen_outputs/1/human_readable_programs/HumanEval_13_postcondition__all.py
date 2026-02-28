
# Response 0
# This postcondition checks that if both inputs `a` and `b` are zero, the `return_value` is 0. Otherwise, it asserts that `return_value` is a positive integer that divides both `a` and `b`, and that no integer larger than `return_value` also divides both `a` and `b`.
assert (a == 0 and b == 0 and return_value == 0) or \
       (return_value > 0 and \
        a % return_value == 0 and \
        b % return_value == 0 and \
        all(not (a % k == 0 and b % k == 0) \
            for k in range(return_value + 1, max(abs(a), abs(b)) + 1)))


