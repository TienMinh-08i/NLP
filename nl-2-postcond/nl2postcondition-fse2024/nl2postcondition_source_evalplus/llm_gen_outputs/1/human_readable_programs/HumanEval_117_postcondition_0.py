# The postcondition verifies that the `return_value` is a list containing exactly all words from the input string `s` that have `n` consonants, maintaining their original order of appearance in `s`.
assert [word for word in filter(None, s.split(" ")) if len(list(filter(lambda ch: ch not in "aeiouAEIOU", word))) == n] == return_value


