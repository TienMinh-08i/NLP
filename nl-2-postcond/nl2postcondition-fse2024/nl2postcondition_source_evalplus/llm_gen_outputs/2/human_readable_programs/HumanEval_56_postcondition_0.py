```python
# The return_value is True if and only if the total number of opening brackets '<' matches the total number of closing brackets '>' and for every prefix of the input string, the number of opening brackets is at least the number of closing brackets.
assert return_value == (brackets.count("<") == brackets.count(">") and all(brackets[:i].count("<") >= brackets[:i].count(">") for i in range(len(brackets) + 1)))
```


