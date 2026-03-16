def is_datetime64_any_dtype_original(arr_or_dtype) -> bool:
    """
    Check whether the provided array or dtype is of the datetime64 dtype.

    Unlike :func:`api.types.is_datetime64_dtype`, this function also
    considers timezone-aware dtypes such as ``DatetimeTZDtype`` to be
    datetime64 dtypes.

    Parameters
    ----------
    arr_or_dtype : array-like or dtype
        The array or dtype to check.

    Returns
    -------
    bool
        Whether or not the array or dtype is of the datetime64 dtype.

    See Also
    --------
    api.types.is_datetime64_dtype : Check whether an array-like or dtype is of the
        datetime64 dtype.
    api.is_datetime64_ns_dtype : Check whether the provided array or dtype is of the
        datetime64[ns] dtype.
    api.is_datetime64tz_dtype : Check whether an array-like or dtype is of a
        DatetimeTZDtype dtype.

    Examples
    --------
    >>> from pandas.api.types import is_datetime64_any_dtype
    >>> from pandas.api.types import DatetimeTZDtype
    >>> is_datetime64_any_dtype(str)
    False
    >>> is_datetime64_any_dtype(int)
    False
    >>> is_datetime64_any_dtype(np.datetime64)  # can be tz-naive
    True
    >>> is_datetime64_any_dtype(DatetimeTZDtype("ns", "US/Eastern"))
    True
    >>> is_datetime64_any_dtype(np.array(["a", "b"]))
    False
    >>> is_datetime64_any_dtype(np.array([1, 2]))
    False
    >>> is_datetime64_any_dtype(np.array([], dtype="datetime64[ns]"))
    True
    >>> is_datetime64_any_dtype(pd.DatetimeIndex([1, 2, 3], dtype="datetime64[ns]"))
    True
    """
    if isinstance(arr_or_dtype, (np.dtype, ExtensionDtype)):
        return arr_or_dtype.kind == 'M'
    if arr_or_dtype is None:
        return False
    try:
        tipo = _get_dtype(arr_or_dtype)
    except TypeError:
        return False
    return lib.is_np_dtype(tipo, 'M') or isinstance(tipo, DatetimeTZDtype) or (isinstance(tipo, ExtensionDtype) and tipo.kind == 'M')


def is_datetime64_any_dtype(arr_or_dtype) -> bool:


    return_value = is_datetime64_any_dtype_original(arr_or_dtype)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition ensures that if is_datetime64_any_dtype returns True, the input is not None and its kind or its dtype's kind is 'M', or its string representation, type, or dtype contains 'datetime64' or 'M8'.
    assert not return_value or (arr_or_dtype is not None and (getattr(arr_or_dtype, 'kind', None) == 'M' or getattr(getattr(arr_or_dtype, 'dtype', None), 'kind', None) == 'M' or any(kw in str(x) for kw in ['datetime64', 'M8'] for x in [arr_or_dtype, type(arr_or_dtype), getattr(arr_or_dtype, 'dtype', None)])))
    

    return return_value
