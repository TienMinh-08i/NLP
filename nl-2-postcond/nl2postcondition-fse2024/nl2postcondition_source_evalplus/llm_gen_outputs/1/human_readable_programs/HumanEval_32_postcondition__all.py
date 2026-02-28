
# Response 0
# The postcondition asserts that evaluating the polynomial with coefficients `xs` at the `return_value` yields a result very close to zero, indicating that `return_value` is a root of the polynomial within a specified tolerance.
assert abs(sum([coeff * math.pow(return_value, i) for i, coeff in enumerate(xs)])) < 1e-3


