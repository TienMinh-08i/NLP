
# Response 0
# The postcondition verifies that return_value is a boolean and that if it is True, the input arr_or_dtype (or its dtype attribute) does not contain keywords indicating non-numeric types such as datetime, timedelta, object, or string.
assert isinstance(return_value, bool) and (not return_value or not any(map(lambda kw: kw in str(getattr(arr_or_dtype, "dtype", arr_or_dtype)).lower(), ["datetime", "timedelta", "object", "str"])))


