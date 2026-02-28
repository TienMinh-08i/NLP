```python
# The postcondition verifies that the return_value is equal to the evaluation of the expression string formed by interleaving the operands and operators.
assert return_value == eval("".join(map(lambda x: str(x[0]) + x[1], zip(operand, operator))) + str(operand[-1]))
```


