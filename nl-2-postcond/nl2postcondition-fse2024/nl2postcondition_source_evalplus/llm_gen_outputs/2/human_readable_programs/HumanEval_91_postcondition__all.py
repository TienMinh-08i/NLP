
# Response 0
# The postcondition verifies that return_value matches the count of sentences (delimited by '.', '?', or '!') that, after stripping whitespace, start with the word "I" followed by a space.
assert return_value == len(list(filter(lambda s: s.startswith("I "), map(lambda x: x.strip(), ((S.replace("?", ".")).replace("!", ".")).split(".")))))


