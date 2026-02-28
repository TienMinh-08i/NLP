
# Response 0
```python
# The postcondition verifies that the return_value is the sum of the digits of the largest prime number in the input list, or None if no prime exists in the list.
assert return_value == (sum(map(int, str(max(filter(lambda x: x > 1 and all(map(lambda i: x % i != 0, range(2, int(x**0.5) + 1))), lst))))) if any(map(lambda x: x > 1 and all(map(lambda i: x % i != 0, range(2, int(x**0.5) + 1))), lst)) else None)
```


