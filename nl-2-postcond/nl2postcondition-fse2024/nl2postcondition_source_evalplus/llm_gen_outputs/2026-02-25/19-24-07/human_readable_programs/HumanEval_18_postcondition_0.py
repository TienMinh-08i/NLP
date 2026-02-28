# This postcondition asserts that the returned value is equal to the count of all indices `i` in the `string` where the `string` slice starting from `i` begins with the given `substring`, thereby verifying the correct count of overlapping occurrences.
assert return_value == sum(1 for i in range(len(string)) if string[i:].startswith(substring))


