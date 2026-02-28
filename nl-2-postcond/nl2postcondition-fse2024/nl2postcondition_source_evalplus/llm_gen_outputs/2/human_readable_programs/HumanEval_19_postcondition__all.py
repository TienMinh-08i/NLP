
# Response 0
# The return_value must be a space-delimited string consisting of the numerals from the input numbers string, sorted in ascending order from 'zero' to 'nine'.
assert return_value == " ".join(sorted(numbers.split(), key=lambda x: {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}[x]))


