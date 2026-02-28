```python
# The postcondition verifies that the first element of the return value is the sum of all integers in the input list,
# and the second element is the product of all integers. It correctly handles an empty list, where the sum is 0 and the product is 1.
from functools import reduce
assert return_value[0] == sum(numbers) and return_value[1] == reduce(lambda x, y: x * y, numbers, 1)
```


