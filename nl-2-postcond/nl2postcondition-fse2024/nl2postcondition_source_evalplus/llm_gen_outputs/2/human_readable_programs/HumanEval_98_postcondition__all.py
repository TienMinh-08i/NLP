
# Response 0
# The postcondition confirms that return_value is the count of uppercase vowels ('A', 'E', 'I', 'O', 'U') at even indices of the string s.
assert return_value == len(list(filter(lambda i: s[i] in "AEIOU", range(0, len(s), 2))))


