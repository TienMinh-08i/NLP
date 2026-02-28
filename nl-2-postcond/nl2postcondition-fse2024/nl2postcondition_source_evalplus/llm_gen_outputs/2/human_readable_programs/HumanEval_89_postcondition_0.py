# The postcondition verifies that return_value has the same length as the input string s and that each lowercase character in s is shifted forward by 4 positions in the alphabet (cyclically), while all other characters remain unchanged.
assert len(return_value) == len(s) and all(c_out == (chr((ord(c_in) - ord('a') + 4) % 26 + ord('a')) if 'a' <= c_in <= 'z' else c_in) for c_in, c_out in zip(s, return_value))


