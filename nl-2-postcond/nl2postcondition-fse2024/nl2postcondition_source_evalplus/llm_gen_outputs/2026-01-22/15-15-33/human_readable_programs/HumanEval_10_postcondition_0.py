# The postcondition asserts that the returned value is a palindrome, starts with the input string,
# and that no shorter string exists which is also a palindrome and starts with the input string.
assert is_palindrome(return_value) and \
       return_value.startswith(string) and \
       all(not is_palindrome(return_value[:k]) for k in range(len(string), len(return_value)))


