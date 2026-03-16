def where_original(cond, left_op, right_op, use_numexpr: bool=True):
    """
    Evaluate the where condition cond on left_op and right_op.

    Parameters
    ----------
    cond : np.ndarray[bool]
    left_op : return if cond is True
    right_op : return if cond is False
    use_numexpr : bool, default True
        Whether to try to use numexpr.
    """
    assert _where is not None
    if use_numexpr:
        return _where(cond, left_op, right_op)
    else:
        return _where_standard(cond, left_op, right_op)


def where(cond, left_op, right_op, use_numexpr: bool=True):


    return_value = where_original(cond, left_op, right_op, use_numexpr)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition ensures that for every index i, the return_value[i] matches left_op[i] if cond[i] is True, and right_op[i] if cond[i] is False.
    assert all(return_value[i] == (left_op[i] if cond[i] else right_op[i]) for i in range(len(cond)))
    

    return return_value
