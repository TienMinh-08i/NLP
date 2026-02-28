
# Response 0
# The postcondition verifies that the returned number of mangoes is equal to the total number of fruits (`n`) minus the number of apples and oranges extracted from the input string `s`.
import re
assert return_value == (n - int(re.search(r"(\d+) apples and (\d+) oranges", s).group(1)) - int(re.search(r"(\d+) apples and (\d+) oranges", s).group(2)))


