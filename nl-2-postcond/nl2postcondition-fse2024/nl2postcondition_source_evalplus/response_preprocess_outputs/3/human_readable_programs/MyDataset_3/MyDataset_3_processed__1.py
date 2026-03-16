def searchsorted_original(arr: ArrayLike, value: NumpyValueArrayLike | ExtensionArray, side: Literal['left', 'right']='left', sorter: NumpySorter | None=None) -> npt.NDArray[np.intp] | np.intp:
    """
    Find indices where elements should be inserted to maintain order.

    Find the indices into a sorted array `arr` (a) such that, if the
    corresponding elements in `value` were inserted before the indices,
    the order of `arr` would be preserved.

    Assuming that `arr` is sorted:

    ======  ================================
    `side`  returned index `i` satisfies
    ======  ================================
    left    ``arr[i-1] < value <= self[i]``
    right   ``arr[i-1] <= value < self[i]``
    ======  ================================

    Parameters
    ----------
    arr: np.ndarray, ExtensionArray, Series
        Input array. If `sorter` is None, then it must be sorted in
        ascending order, otherwise `sorter` must be an array of indices
        that sort it.
    value : array-like or scalar
        Values to insert into `arr`.
    side : {'left', 'right'}, optional
        If 'left', the index of the first suitable location found is given.
        If 'right', return the last such index.  If there is no suitable
        index, return either 0 or N (where N is the length of `self`).
    sorter : 1-D array-like, optional
        Optional array of integer indices that sort array a into ascending
        order. They are typically the result of argsort.

    Returns
    -------
    array of ints or int
        If value is array-like, array of insertion points.
        If value is scalar, a single integer.

    See Also
    --------
    numpy.searchsorted : Similar method from NumPy.
    """
    if sorter is not None:
        sorter = ensure_platform_int(sorter)
    if isinstance(arr, np.ndarray) and arr.dtype.kind in 'iu' and (is_integer(value) or is_integer_dtype(value)):
        iinfo = np.iinfo(arr.dtype.type)
        value_arr = np.array([value]) if is_integer(value) else np.array(value)
        if (value_arr >= iinfo.min).all() and (value_arr <= iinfo.max).all():
            dtype = arr.dtype
        else:
            dtype = value_arr.dtype
        if is_integer(value):
            value = cast('int', dtype.type(value))
        else:
            value = pd_array(cast('ArrayLike', value), dtype=dtype)
    else:
        arr = ensure_wrapped_if_datetimelike(arr)
    return arr.searchsorted(value, side=side, sorter=sorter)


def searchsorted(arr: ArrayLike, value: NumpyValueArrayLike | ExtensionArray, side: Literal['left', 'right']='left', sorter: NumpySorter | None=None) -> npt.NDArray[np.intp] | np.intp:


    return_value = searchsorted_original(arr, value, side, sorter)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition verifies that for each value 'v' and its corresponding insertion index 'idx' in 'return_value',
    # the sorted version of 'arr' (using 'sorter' if provided) is correctly partitioned at 'idx' based on the 'side' parameter:
    # elements before 'idx' are < v (side='left') or <= v (side='right'), and elements at or after 'idx' are >= v (side='left') or > v (side='right').
    assert all(
        all((S[sorter[j] if sorter is not None else j] < v if side == 'left' else S[sorter[j] if sorter is not None else j] <= v) for j in range(idx)) and
        all((S[sorter[j] if sorter is not None else j] >= v if side == 'left' else S[sorter[j] if sorter is not None else j] > v) for j in range(idx, len(arr)))
        for S in [getattr(arr, 'iloc', arr)]
        for v, idx in (zip(value, return_value) if hasattr(return_value, '__iter__') else [(value, return_value)])
    )
    

    return return_value
