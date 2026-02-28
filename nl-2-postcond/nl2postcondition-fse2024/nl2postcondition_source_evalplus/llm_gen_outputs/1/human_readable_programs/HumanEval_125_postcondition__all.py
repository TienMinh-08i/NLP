
# Response 0
# The postcondition asserts that the return_value correctly reflects the branching logic of the split_words function.
# If the input text contains any whitespace, the return_value must be the list of words split by whitespace.
# Otherwise, if the input text contains a comma, the return_value must be the list of words split by commas.
# Otherwise (no whitespace and no commas), the return_value must be the count of lowercase letters in the text
# whose alphabetical order (0-indexed from 'a') is odd.
assert (any(ws_char in txt for ws_char in ' \n\r\t') and return_value == txt.split()) or \
       (not any(ws_char in txt for ws_char in ' \n\r\t') and ',' in txt and return_value == txt.split(',')) or \
       (not any(ws_char in txt for ws_char in ' \n\r\t') and ',' not in txt and return_value == sum(1 for ch in txt if ch.islower() and (ord(ch) - ord('a')) % 2 == 1))


