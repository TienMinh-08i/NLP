
# Response 0
# The postcondition verifies that if the side lengths a, b, and c form a valid triangle, the return_value is the area of the triangle calculated using Heron's formula and rounded to two decimal places; otherwise, the return_value is -1.
assert return_value == (round(((a + b + c) / 2 * ((a + b + c) / 2 - a) * ((a + b + c) / 2 - b) * ((a + b + c) / 2 - c)) ** 0.5, 2) if a + b > c and a + c > b and b + c > a else -1)


