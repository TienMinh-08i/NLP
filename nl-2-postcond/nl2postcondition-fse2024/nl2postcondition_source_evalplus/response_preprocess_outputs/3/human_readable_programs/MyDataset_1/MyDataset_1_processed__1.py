def isin_original(comps: ListLike, values: ListLike) -> npt.NDArray[np.bool_]:
    """
    Compute the isin boolean array.

    Parameters
    ----------
    comps : list-like
    values : list-like

    Returns
    -------
    ndarray[bool]
        Same length as `comps`.
    """
    if not is_list_like(comps):
        raise TypeError(f'only list-like objects are allowed to be passed to isin(), you passed a `{type(comps).__name__}`')
    if not is_list_like(values):
        raise TypeError(f'only list-like objects are allowed to be passed to isin(), you passed a `{type(values).__name__}`')
    if not isinstance(values, (ABCIndex, ABCSeries, ABCExtensionArray, np.ndarray)):
        orig_values = list(values)
        values = _ensure_arraylike(orig_values, func_name='isin-targets')
        if len(values) > 0 and values.dtype.kind in 'iufcb' and (not is_signed_integer_dtype(comps)) and (not is_dtype_equal(values, comps)):
            values = construct_1d_object_array_from_listlike(orig_values)
    elif isinstance(values, ABCMultiIndex):
        values = np.array(values)
    else:
        values = extract_array(values, extract_numpy=True, extract_range=True)
    comps_array = _ensure_arraylike(comps, func_name='isin')
    comps_array = extract_array(comps_array, extract_numpy=True)
    if not isinstance(comps_array, np.ndarray):
        return comps_array.isin(values)
    elif needs_i8_conversion(comps_array.dtype):
        return pd_array(comps_array).isin(values)
    elif needs_i8_conversion(values.dtype) and (not is_object_dtype(comps_array.dtype)):
        return np.zeros(comps_array.shape, dtype=bool)
    elif needs_i8_conversion(values.dtype):
        return isin(comps_array, values.astype(object))
    elif isinstance(values.dtype, ExtensionDtype):
        return isin(np.asarray(comps_array), np.asarray(values))
    if len(comps_array) > _MINIMUM_COMP_ARR_LEN and len(values) <= 26 and (comps_array.dtype != object) and (not any((v is NA for v in values))):
        if isna(values).any():

            def f(c, v):
                return np.logical_or(np.isin(c, v).ravel(), np.isnan(c))
        else:
            f = lambda a, b: np.isin(a, b).ravel()
    else:
        common = np_find_common_type(values.dtype, comps_array.dtype)
        values = values.astype(common, copy=False)
        comps_array = comps_array.astype(common, copy=False)
        f = htable.ismember
    return f(comps_array, values)


def isin(comps: ListLike, values: ListLike) -> npt.NDArray[np.bool_]:


    return_value = isin_original(comps, values)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition verifies that return_value is a boolean array with the same length as comps,
    # where each element correctly indicates if the corresponding element in comps is present in values,
    # specifically handling equality matches, identity matches (for None and pd.NA), and NaN-to-NaN matches.
    comps_list = list(comps)
    values_list = list(values)
    assert len(return_value) == len(comps_list) and all(
        res == any((c is v) or ((c == v) == True) is True or ((c != c and v != v) is True) for v in values_list)
        for res, c in zip(return_value, comps_list)
    )

    return return_value
