```python
# If the return value is True, then arr_or_dtype must not be None and its resolved dtype (as a string) must indicate a datetime64 type with nanosecond resolution.
import re
assert not return_value or (arr_or_dtype is not None and re.search(r'datetime64.*ns', str(getattr(arr_or_dtype, "dtype", arr_or_dtype))) is not None)
```


