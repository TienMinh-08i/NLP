
# Response 0
# The postcondition verifies that the returned string has the same length as the input string.
# It then checks each character: if the original character is a lowercase letter, the corresponding returned character must be shifted by 4 positions (wrapping around the alphabet); otherwise, the returned character must be identical to the original.
assert len(s) == len(return_value) and \
       all(char_s == char_r if not char_s.islower() else \
           ord(char_r) == (ord(char_s) - ord('a') + 4) % 26 + ord('a') \
           for char_s, char_r in zip(s, return_value))


