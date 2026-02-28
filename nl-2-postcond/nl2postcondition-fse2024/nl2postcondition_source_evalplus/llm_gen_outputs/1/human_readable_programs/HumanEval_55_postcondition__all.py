
# Response 0
```python
import functools

# Postcondition: Checks if the returned value matches the n-th Fibonacci number.
# It handles the base case for n=0 directly. For n >= 1, it iteratively computes
# the n-th Fibonacci number using functools.reduce, mimicking the sequence generation,
# and compares it with the return_value.
assert (n == 0 and return_value == 0) or \
       (n >= 1 and functools.reduce(lambda acc, _: (acc[1], acc[0] + acc[1]), range(n - 1), (0, 1))[1] == return_value)
```


