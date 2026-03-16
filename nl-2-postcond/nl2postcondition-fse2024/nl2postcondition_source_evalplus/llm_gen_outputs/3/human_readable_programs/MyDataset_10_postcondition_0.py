# The postcondition verifies that return_value is True if and only if the input or its dtype attribute has a kind of 'M' (NumPy's datetime64 indicator), if it is a subclass of the np.datetime64 class, or if it is a string representing a non-timezone-aware datetime64 dtype.
import re
assert return_value == (
    (getattr(getattr(arr_or_dtype, 'dtype', arr_or_dtype), 'kind', None) == 'M') or
    (isinstance(arr_or_dtype, type) and issubclass(arr_or_dtype, np.datetime64)) or
    (isinstance(arr_or_dtype, str) and bool(re.match(r'^([<>])?(datetime64|M8)(\[[^,\]]+\])?$', arr_or_dtype)))
)


