
# Response 0
# The postcondition ensures that the return value is True if and only if the input is a numeric dtype and is neither a complex nor a boolean dtype.
assert return_value == (is_numeric_dtype(arr_or_dtype) and not is_complex_dtype(arr_or_dtype) and not is_bool_dtype(arr_or_dtype))


