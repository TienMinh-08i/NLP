
# Response 0
# The postcondition checks if the return_value is -1 when the sides do not form a valid triangle,
# and otherwise checks if the return_value is the correctly calculated area rounded to 2 decimal places using Heron's formula.
assert (return_value == -1 if (a + b <= c or a + c <= b or b + c <= a) else return_value == round(((a + b + c) / 2 * ((a + b + c) / 2 - a) * ((a + b + c) / 2 - b) * ((a + b + c) / 2 - c)) ** 0.5, 2))


