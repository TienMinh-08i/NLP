```python
# The postcondition verifies that return_value is 0 if n contains no odd digits, and otherwise equals the product of all its odd digits.
assert return_value == (0 if not __import__('re').findall('[13579]', str(n)) else __import__('math').prod(map(int, __import__('re').findall('[13579]', str(n)))))
```


