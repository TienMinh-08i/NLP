```python
# The n-th Fibonacci number is equal to the sum of the binomial coefficients (n-k-1 choose k) for k from 0 to floor((n-1)/2).
assert return_value == sum(__import__('math').comb(n - k - 1, k) for k in range((n + 1) // 2))
```


