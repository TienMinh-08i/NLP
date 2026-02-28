# The return_value is True if and only if string b is empty or at least one of its cyclic rotations is a substring of string a.
assert return_value == (b == "" or any(b[i:] + b[:i] in a for i in range(len(b))))


