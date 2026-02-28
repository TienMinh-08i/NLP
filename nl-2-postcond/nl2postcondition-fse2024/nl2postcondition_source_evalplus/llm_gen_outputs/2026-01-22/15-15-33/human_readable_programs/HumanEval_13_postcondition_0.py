```python
# The postcondition asserts properties of the greatest common divisor (GCD).
# If both input integers 'a' and 'b' are zero, the GCD ('return_value') must be zero.
# Otherwise (if at least one of 'a' or 'b' is non-zero), the GCD ('return_value') must be a positive integer
# that divides both 'a' and 'b', and no integer greater than 'return_value' should also divide both 'a' and 'b'.
assert (a == 0 and b == 0 and return_value == 0) or \
       ((a != 0 or b != 0) and \
        return_value > 0 and \
        a % return_value == 0 and \
        b % return_value == 0 and \
        all(not (a % k == 0 and b % k == 0) for k in range(return_value + 1, max(abs(a), abs(b)) + 1)))
```


