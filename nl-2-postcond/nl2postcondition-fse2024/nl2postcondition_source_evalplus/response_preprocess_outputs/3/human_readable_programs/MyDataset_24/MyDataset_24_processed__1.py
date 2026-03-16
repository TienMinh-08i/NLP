def is_any_real_numeric_dtype_original(arr_or_dtype) -> bool:
    """
    Check whether the provided array or dtype is of a real number dtype.

    Real number dtypes include integer and float types but exclude complex
    and boolean dtypes. This is useful when operations require real-valued
    numeric input only.

    Parameters
    ----------
    arr_or_dtype : array-like or dtype
        The array or dtype to check.

    Returns
    -------
    boolean
        Whether or not the array or dtype is of a real number dtype.

    See Also
    --------
    is_numeric_dtype : Check if a dtype is numeric.
    is_complex_dtype : Check if a dtype is complex.
    is_bool_dtype : Check if a dtype is boolean.

    Examples
    --------
    >>> from pandas.api.types import is_any_real_numeric_dtype
    >>> is_any_real_numeric_dtype(int)
    True
    >>> is_any_real_numeric_dtype(float)
    True
    >>> is_any_real_numeric_dtype(object)
    False
    >>> is_any_real_numeric_dtype(str)
    False
    >>> is_any_real_numeric_dtype(complex(1, 2))
    False
    >>> is_any_real_numeric_dtype(bool)
    False
    """
    return is_numeric_dtype(arr_or_dtype) and (not is_complex_dtype(arr_or_dtype)) and (not is_bool_dtype(arr_or_dtype))


def is_any_real_numeric_dtype(arr_or_dtype) -> bool:


    return_value = is_any_real_numeric_dtype_original(arr_or_dtype)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition ensures that the return value is True if and only if the input is a numeric dtype and is neither a complex nor a boolean dtype.
    assert return_value == (is_numeric_dtype(arr_or_dtype) and not is_complex_dtype(arr_or_dtype) and not is_bool_dtype(arr_or_dtype))

    return return_value
