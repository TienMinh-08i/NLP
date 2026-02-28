
# Response 0
# The postcondition verifies that the return_value is equal to the input text with all uppercase and lowercase vowels removed, maintaining the original order of the remaining characters.
assert return_value == "".join(filter(lambda ch: ch not in "aeiouAEIOU", text))


