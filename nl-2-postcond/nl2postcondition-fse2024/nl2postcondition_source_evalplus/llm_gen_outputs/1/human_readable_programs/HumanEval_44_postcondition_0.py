# The postcondition asserts that the `return_value` is a valid string representation of `x` in the given `base`.
# This means that all digits in `return_value` are valid for the `base` (i.e., less than `base`), and when `return_value` is converted back to base 10, it equals the original number `x`.
# It also ensures that there are no leading zeros, unless `x` itself is 0.
assert (x == 0 and return_value == "0") or \
       (x > 0 and \
        len(return_value) > 0 and \
        return_value[0] != '0' and \
        all(int(digit) < base for digit in return_value) and \
        sum(int(digit) * (base ** power) for power, digit in enumerate(reversed(return_value))) == x)


