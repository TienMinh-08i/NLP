# The postcondition asserts that the returned value is True if and only if any permutation of the sides satisfies the Pythagorean theorem (a^2 + b^2 = c^2), indicating a right-angled triangle. Otherwise, the returned value must be False.
assert return_value == (a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2)


