# The postcondition asserts three properties of the `return_value` from `make_palindrome` given the input `string`:
# 1. The `return_value` itself must be a palindrome.
# 2. The `return_value` must begin with the original `string`.
# 3. The `return_value` must be the shortest possible string satisfying the first two conditions. This is ensured by checking that no proper prefix of `return_value` (which is also longer than the original `string`) is a palindrome.
assert (is_palindrome(return_value) and
        return_value.startswith(string) and
        all(not is_palindrome(return_value[:k])
            for k in range(len(string) + 1, len(return_value))))


