```
# The postcondition asserts that the returned value is present in the input list and is greater than or equal to every other element in the list.
assert return_value in l and all(return_value >= x for x in l)
```


