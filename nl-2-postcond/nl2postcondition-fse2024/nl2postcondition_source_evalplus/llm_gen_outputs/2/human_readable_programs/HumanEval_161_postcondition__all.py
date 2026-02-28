
# Response 0
# The return_value is the string s with the case of each letter swapped if s contains at least one letter, otherwise it is the reverse of s.
assert return_value == ("".join(c.swapcase() if c.isalpha() else c for c in s) if any(c.isalpha() for c in s) else s[::-1])


