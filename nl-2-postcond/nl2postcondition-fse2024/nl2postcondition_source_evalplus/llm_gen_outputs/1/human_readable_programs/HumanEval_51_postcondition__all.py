
# Response 0
# The postcondition asserts that the returned string is exactly what is obtained by filtering out all vowels (case-insensitive) from the input string, thus ensuring all non-vowel characters are preserved in order and no vowels are present.
assert return_value == "".join(filter(lambda ch: ch not in "aeiouAEIOU", text))


