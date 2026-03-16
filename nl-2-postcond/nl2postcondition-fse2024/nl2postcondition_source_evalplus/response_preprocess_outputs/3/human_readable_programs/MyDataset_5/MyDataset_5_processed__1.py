def contains_original(cat, key, container) -> bool:
    """
    Helper for membership check for ``key`` in ``cat``.

    This is a helper method for :meth:`__contains__`
    and :class:`CategoricalIndex.__contains__`.

    Returns True if ``key`` is in ``cat.categories`` and the
    location of ``key`` in ``categories`` is in ``container``.

    Parameters
    ----------
    cat : :class:`Categorical`or :class:`CategoricalIndex`
    key : a hashable object
        The key to check membership for.
    container : Container (e.g. list-like or mapping)
        The container to check for membership in.

    Returns
    -------
    is_in : bool
        True if ``key`` is in ``self.categories`` and location of
        ``key`` in ``categories`` is in ``container``, else False.

    Notes
    -----
    This method does not check for NaN values. Do that separately
    before calling this method.
    """
    hash(key)
    try:
        loc = cat.categories.get_loc(key)
    except (KeyError, TypeError):
        return False
    if is_scalar(loc):
        return loc in container
    else:
        return any((loc_ in container for loc_ in loc))


def contains(cat, key, container) -> bool:


    return_value = contains_original(cat, key, container)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The return_value is True if and only if key is in cat.categories and its position (or one of its positions) as determined by get_loc is in the container.
    assert return_value == ((key in cat.categories) and (lambda loc: any(l in container for l in loc) if hasattr(loc, '__iter__') else loc in container)(cat.categories.get_loc(key)))

    return return_value
