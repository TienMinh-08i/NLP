
# Response 0
# The postcondition ensures that return_value is True if and only if the last character of the string is an alphabetical letter and it is either the only character in the string or is preceded by a space.
assert return_value == (len(txt) > 0 and txt[-1].isalpha() and (len(txt) == 1 or txt[-2] == " "))


