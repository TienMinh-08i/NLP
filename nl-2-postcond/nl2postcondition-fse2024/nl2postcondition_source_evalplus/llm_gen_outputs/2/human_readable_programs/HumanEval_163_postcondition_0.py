# The return_value is equal to the list of all even digits that fall within the range [min(a, b), max(a, b)], sorted in ascending order.
assert return_value == list(filter(lambda x: x % 2 == 0, range(min(a, b), min(max(a, b) + 1, 10))))


