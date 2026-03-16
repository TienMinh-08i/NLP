def is_categorical_dtype_original(arr_or_dtype) -> bool:
    """
    Check whether an array-like or dtype is of the Categorical dtype.

    .. deprecated:: 2.2.0
        Use isinstance(dtype, pd.CategoricalDtype) instead.

    Parameters
    ----------
    arr_or_dtype : array-like or dtype
        The array-like or dtype to check.

    Returns
    -------
    boolean
        Whether or not the array-like or dtype is of the Categorical dtype.

    See Also
    --------
    api.types.is_list_like: Check if the object is list-like.
    api.types.is_complex_dtype: Check whether the provided array or
                                dtype is of a complex dtype.

    Examples
    --------
    >>> from pandas.api.types import is_categorical_dtype
    >>> from pandas import CategoricalDtype
    >>> is_categorical_dtype(object)
    False
    >>> is_categorical_dtype(CategoricalDtype())
    True
    >>> is_categorical_dtype([1, 2, 3])
    False
    >>> is_categorical_dtype(pd.Categorical([1, 2, 3]))
    True
    >>> is_categorical_dtype(pd.CategoricalIndex([1, 2, 3]))
    True
    """
    warnings.warn('is_categorical_dtype is deprecated and will be removed in a future version. Use isinstance(dtype, pd.CategoricalDtype) instead', Pandas4Warning, stacklevel=2)
    if isinstance(arr_or_dtype, ExtensionDtype):
        return arr_or_dtype.name == 'category'
    if arr_or_dtype is None:
        return False
    return CategoricalDtype.is_dtype(arr_or_dtype)


def is_categorical_dtype(arr_or_dtype) -> bool:


    return_value = is_categorical_dtype_original(arr_or_dtype)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The return_value is True if and only if the input arr_or_dtype is not None and either it is an ExtensionDtype with the name 'category' or it satisfies the CategoricalDtype.is_dtype check.
    assert return_value == (arr_or_dtype.name == 'category' if isinstance(arr_or_dtype, ExtensionDtype) else (False if arr_or_dtype is None else CategoricalDtype.is_dtype(arr_or_dtype)))
    

    return return_value
