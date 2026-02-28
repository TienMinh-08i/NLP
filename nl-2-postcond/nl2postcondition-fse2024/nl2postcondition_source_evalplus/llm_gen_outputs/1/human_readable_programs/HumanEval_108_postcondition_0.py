# The postcondition asserts that the returned value is the count of numbers in the input array
# for which the sum of their signed digits is greater than zero.
# For negative numbers (e.g., -123), the first digit after the sign is considered negative (-1),
# while subsequent digits are positive (2, 3), resulting in a sum of -1 + 2 + 3 = 4.
assert return_value == sum(
    1 for n in arr
    if sum(
        ([-int(str(n)[1])] + list(map(int, str(n)[2:]))) # For negative numbers, e.g., -123 -> -1, 2, 3
        if str(n)[0] == '-'
        else list(map(int, str(n))) # For positive numbers, e.g., 123 -> 1, 2, 3
    ) > 0
)


