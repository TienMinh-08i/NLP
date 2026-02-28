# This postcondition asserts that the returned tuple `return_value` correctly represents the count of even and odd integer palindromes within the range [1, n], inclusive.
assert return_value == (len(list(filter(lambda x: str(x) == str(x)[::-1] and x % 2 == 0, range(1, n + 1)))), len(list(filter(lambda x: str(x) == str(x)[::-1] and x % 2 == 1, range(1, n + 1)))))


