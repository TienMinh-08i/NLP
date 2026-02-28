# The postcondition checks that if the input text is empty, the return value is None. Otherwise, it asserts that the return value is a 32-character hexadecimal string (lowercase a-f).
import re
assert (text == "" and return_value is None) or \
       (text != "" and isinstance(return_value, str) and len(return_value) == 32 and bool(re.fullmatch(r'^[0-9a-f]{32}$', return_value)))


