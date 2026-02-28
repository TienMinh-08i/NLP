# The postcondition ensures that return_value is a list of all non-empty words from the string s 
# (where words are delimited by single spaces) that contain exactly n consonants 
# (any character not in "aeiouAEIOU"), preserving their original order of appearance.
assert return_value == [word for word in s.split(" ") if word != "" and len(list(filter(lambda ch: ch not in "aeiouAEIOU", word))) == n]


