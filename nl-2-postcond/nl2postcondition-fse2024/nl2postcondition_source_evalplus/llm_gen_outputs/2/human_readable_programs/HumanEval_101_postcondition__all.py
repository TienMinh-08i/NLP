
# Response 0
# The postcondition checks that return_value matches the list of all substrings in s that consist of characters other than commas and whitespace.
import re
assert return_value == re.findall(r'[^,\s]+', s)


