```python
# The postcondition verifies that the polynomial evaluated at the return_value is approximately zero.
assert abs(sum(coeff * pow(return_value, i) for i, coeff in enumerate(xs))) < 1e-2
```


