def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome_original(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if is_palindrome(string):
        return string
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            return string + string[i - 1::-1]


def make_palindrome(string: str) -> str:


    return_value = make_palindrome_original(string)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition asserts three properties of the `return_value` from `make_palindrome` given the input `string`:
    # 1. The `return_value` itself must be a palindrome.
    # 2. The `return_value` must begin with the original `string`.
    # 3. The `return_value` must be the shortest possible string satisfying the first two conditions. This is ensured by checking that no proper prefix of `return_value` (which is also longer than the original `string`) is a palindrome.
    assert (is_palindrome(return_value) and
            return_value.startswith(string) and
            all(not is_palindrome(return_value[:k])
                for k in range(len(string) + 1, len(return_value))))

    return return_value
