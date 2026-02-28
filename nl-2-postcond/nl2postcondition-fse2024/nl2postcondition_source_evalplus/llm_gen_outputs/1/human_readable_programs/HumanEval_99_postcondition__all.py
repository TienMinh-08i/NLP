
# Response 0
# This postcondition asserts that the `return_value` is the closest integer to the input `value` (converted to a float), following a specific rounding rule: if the number is equidistant from two integers (i.e., its fractional part is 0.5), it is rounded away from zero; otherwise, it is rounded to the nearest integer.
assert (
    (abs(float(value) - int(float(value))) != 0.5 and return_value == round(float(value))) or
    (abs(float(value) - int(float(value))) == 0.5 and float(value) > 0 and return_value == int(float(value)) + 1) or
    (abs(float(value) - int(float(value))) == 0.5 and float(value) <= 0 and return_value == int(float(value)) - 1)
)


