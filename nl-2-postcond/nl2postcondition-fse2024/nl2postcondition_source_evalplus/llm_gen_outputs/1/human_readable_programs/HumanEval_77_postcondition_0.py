# This postcondition checks that the function's return value is True if and only if the absolute value of the input `a` is a perfect cube of an integer.
assert return_value == (int(round(abs(a) ** (1.0 / 3.0))) ** 3 == abs(a))


