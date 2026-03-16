# If the return value is True, the input arr_or_dtype must not be None and its dtype (or the input itself if it is already a dtype) must have a string representation containing 'datetime64[ns'.
assert not return_value or (arr_or_dtype is not None and "datetime64[ns" in str(getattr(arr_or_dtype, "dtype", arr_or_dtype)))


