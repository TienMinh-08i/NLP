
# Response 0
# The postcondition asserts that the return_value is equal to the count of sentences in the input string S that start with "I " (case-sensitive).
# Sentences are identified by first replacing '?' and '!' with '.', then splitting the string by '.', and finally stripping leading/trailing whitespace from each segment.
assert return_value == len(list(filter(lambda s: s.startswith("I "), map(lambda x: x.strip(), S.replace("?", ".").replace("!", ".").split(".")))))


