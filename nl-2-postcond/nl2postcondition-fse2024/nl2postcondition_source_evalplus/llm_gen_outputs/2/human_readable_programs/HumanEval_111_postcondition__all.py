
# Response 0
# The return_value must be a dictionary that contains all words from the input string 'test' that occur with the maximum frequency, mapping each such word to its count.
assert return_value == {w: test.split().count(w) for w in set(test.split()) if test.split().count(w) == max([test.split().count(x) for x in set(test.split())] or [0])}


