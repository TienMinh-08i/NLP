
# Response 0
# The postcondition verifies that return_value is True if and only if the product of the numerators of fractions x and n is divisible by the product of their denominators.
assert return_value == ((int(x.split("/")[0]) * int(n.split("/")[0])) % (int(x.split("/")[1]) * int(n.split("/")[1])) == 0)


