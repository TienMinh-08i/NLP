
# Response 0
# The return_value must be the integer closest to the float representation of the input string, rounding away from zero in case of ties.
assert return_value == int(return_value) and (abs(float(value) - return_value) < 0.5 or (abs(float(value) - return_value) == 0.5 and abs(return_value) > abs(float(value))))


