
# Response 0
# The postcondition asserts that the return value is True if the input string has exactly one character and that character is a letter, OR if the input string has more than one character, its last character is a letter, and the character before it is a space. Otherwise, the return value is False.
assert return_value == ((len(txt) == 1 and txt[0].isalpha()) or (len(txt) > 1 and txt[-1].isalpha() and txt[-2] == " "))


