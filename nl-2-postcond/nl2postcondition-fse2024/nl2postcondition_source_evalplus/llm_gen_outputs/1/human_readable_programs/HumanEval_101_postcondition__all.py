
# Response 0
# This postcondition asserts that the returned list of words is identical to the list obtained by first replacing all commas in the input string with spaces, then splitting the resulting string by any whitespace, and finally filtering out any empty strings.
assert return_value == list(filter(lambda word: word != "", s.replace(",", " ").split()))


