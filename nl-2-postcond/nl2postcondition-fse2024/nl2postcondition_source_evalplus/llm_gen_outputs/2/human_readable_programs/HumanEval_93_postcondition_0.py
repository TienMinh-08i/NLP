# The postcondition verifies that the length of return_value matches the length of message and that each character in return_value is the case-swapped version of the corresponding character in message, with an additional shift of two positions in the alphabet if that case-swapped character is a vowel.
assert len(return_value) == len(message) and all(rv == (chr(ord(m.swapcase()) + 2) if m.swapcase() in "aeiouAEIOU" else m.swapcase()) for m, rv in zip(message, return_value))


