# Checks that the returned list contains only elements that appeared exactly once in the input list, and that their original relative order is preserved.
assert return_value == [number for number in numbers if numbers.count(number) == 1]


