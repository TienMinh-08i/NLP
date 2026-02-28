# The postcondition verifies that return_value is the count of vowels ('a', 'e', 'i', 'o', 'u', case-insensitive) in 's', plus 1 if 's' ends with 'y' or 'Y'.
assert return_value == len(list(filter(lambda ch: ch in 'aeiouAEIOU', s))) + (1 if s[-1:] in ('y', 'Y') else 0)


