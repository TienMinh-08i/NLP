# The postcondition asserts that the returned list contains only the elements from the input list that appeared exactly once, preserving their original relative order.
assert return_value == [x for x in numbers if numbers.count(x) == 1]


