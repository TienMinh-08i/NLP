# The postcondition asserts that the `return_value` is equal to the evaluation of the algebraic expression constructed by interleaving the string representations of the operands with the operators.
assert eval("".join([str(operand[i]) + operator[i] for i in range(len(operator))]) + str(operand[-1])) == return_value


