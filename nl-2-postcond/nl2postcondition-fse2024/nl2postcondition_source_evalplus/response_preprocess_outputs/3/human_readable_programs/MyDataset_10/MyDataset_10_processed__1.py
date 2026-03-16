def is_datetime64_dtype_original(arr_or_dtype) -> bool:
    """
    Check whether an array-like or dtype is of the datetime64 dtype.

    This function checks for the base ``datetime64`` dtype without regard
    to timezone information. For timezone-aware checks, use
    :func:`api.types.is_datetime64_any_dtype` instead.

    Parameters
    ----------
    arr_or_dtype : array-like or dtype
        The array-like or dtype to check.

    Returns
    -------
    boolean
        Whether or not the array-like or dtype is of the datetime64 dtype.

    See Also
    --------
    api.types.is_datetime64_ns_dtype: Check whether the provided array or
                                        dtype is of the datetime64[ns] dtype.
    api.types.is_datetime64_any_dtype: Check whether the provided array or
                                        dtype is of the datetime64 dtype.

    Examples
    --------
    >>> from pandas.api.types import is_datetime64_dtype
    >>> is_datetime64_dtype(object)
    False
    >>> is_datetime64_dtype(np.datetime64)
    True
    >>> is_datetime64_dtype(np.array([], dtype=int))
    False
    >>> is_datetime64_dtype(np.array([], dtype=np.datetime64))
    True
    >>> is_datetime64_dtype([1, 2, 3])
    False
    """
    if isinstance(arr_or_dtype, np.dtype):
        return arr_or_dtype.kind == 'M'
    return _is_dtype_type(arr_or_dtype, classes(np.datetime64))


def is_datetime64_dtype(arr_or_dtype) -> bool:


    return_value = is_datetime64_dtype_original(arr_or_dtype)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition verifies that return_value is True if and only if the input or its dtype attribute has a kind of 'M' (NumPy's datetime64 indicator), if it is a subclass of the np.datetime64 class, or if it is a string representing a non-timezone-aware datetime64 dtype.
    import re
    assert return_value == (
        (getattr(getattr(arr_or_dtype, 'dtype', arr_or_dtype), 'kind', None) == 'M') or
        (isinstance(arr_or_dtype, type) and issubclass(arr_or_dtype, np.datetime64)) or
        (isinstance(arr_or_dtype, str) and bool(re.match(r'^([<>])?(datetime64|M8)(\[[^,\]]+\])?$', arr_or_dtype)))
    )

    return return_value
