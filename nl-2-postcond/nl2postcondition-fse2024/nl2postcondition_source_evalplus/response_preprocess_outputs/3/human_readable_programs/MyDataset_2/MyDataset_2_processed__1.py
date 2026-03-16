def duplicated_original(values: ArrayLike, keep: Literal['first', 'last', False]='first', mask: npt.NDArray[np.bool_] | None=None) -> npt.NDArray[np.bool_]:
    """
    Return boolean ndarray denoting duplicate values.

    Parameters
    ----------
    values : np.ndarray or ExtensionArray
        Array over which to check for duplicate values.
    keep : {'first', 'last', False}, default 'first'
        - ``first`` : Mark duplicates as ``True`` except for the first
          occurrence.
        - ``last`` : Mark duplicates as ``True`` except for the last
          occurrence.
        - False : Mark all duplicates as ``True``.
    mask : ndarray[bool], optional
        array indicating which elements to exclude from checking

    Returns
    -------
    duplicated : ndarray[bool]
    """
    values = _ensure_data(values)
    return htable.duplicated(values, keep=keep, mask=mask)


def duplicated(values: ArrayLike, keep: Literal['first', 'last', False]='first', mask: npt.NDArray[np.bool_] | None=None) -> npt.NDArray[np.bool_]:


    return_value = duplicated_original(values, keep, mask)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition ensures that return_value[i] is True if and only if the element at index i is not masked and there exists another unmasked index j such that values[i] == values[j], where the index j satisfies the 'keep' condition: j < i for 'first', j > i for 'last', or j != i for False.
    assert all(return_value[i] == ((mask is None or not mask[i]) and any((mask is None or not mask[j]) and values[i] == values[j] for j in range(len(values)) if (j < i if keep == 'first' else j > i if keep == 'last' else j != i))) for i in range(len(values)))

    return return_value
