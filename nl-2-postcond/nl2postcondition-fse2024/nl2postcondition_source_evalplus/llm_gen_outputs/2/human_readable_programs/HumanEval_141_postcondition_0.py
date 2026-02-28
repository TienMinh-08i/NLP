# The postcondition verifies that return_value is "Yes" if and only if the file_name contains no more than three digits, exactly one dot, starts with a latin alphabet letter, and ends with a valid extension ('txt', 'exe', or 'dll').
import re
assert return_value == ("Yes" if (len(list(filter(lambda c: c.isdigit(), file_name))) <= 3 and bool(re.match(r'^[a-zA-Z][^.]*\.(txt|exe|dll)$', file_name))) else "No")


