
# Response 0
# The return value must be a boolean, and if both source and target are the same common dtype string, return_value must be True.
import re
assert isinstance(return_value, bool) and (not (isinstance(source, str) and isinstance(target, str) and source == target and re.match(r'^(int|float|bool|category|object|datetime64|timedelta64)$', source)) or return_value)


