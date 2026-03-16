def col_original(col_name: Hashable) -> Expression:
    """
    Generate deferred object representing a column of a DataFrame.

    Any place which accepts ``lambda df: df[col_name]``, such as
    :meth:`DataFrame.assign` or :meth:`DataFrame.loc`, can also accept
    ``pd.col(col_name)``.

    .. versionadded:: 3.0.0

    Parameters
    ----------
    col_name : Hashable
        Column name.

    Returns
    -------
    `pandas.api.typing.Expression`
        A deferred object representing a column of a DataFrame.

    See Also
    --------
    DataFrame.query : Query columns of a dataframe using string expressions.

    Examples
    --------

    You can use `col` in `assign`.

    >>> df = pd.DataFrame({"name": ["beluga", "narwhal"], "speed": [100, 110]})
    >>> df.assign(name_titlecase=pd.col("name").str.title())
          name  speed name_titlecase
    0   beluga    100         Beluga
    1  narwhal    110        Narwhal

    You can also use it for filtering.

    >>> df.loc[pd.col("speed") > 105]
          name  speed
    1  narwhal    110
    """
    if not isinstance(col_name, Hashable):
        msg = f'Expected Hashable, got: {type(col_name)}'
        raise TypeError(msg)

    def func(df: DataFrame) -> Series:
        if col_name not in df.columns:
            columns_str = str(df.columns.tolist())
            max_len = 90
            if len(columns_str) > max_len:
                columns_str = columns_str[:max_len] + '...]'
            msg = f"Column '{col_name}' not found in given DataFrame.\n\nHint: did you mean one of {columns_str} instead?"
            raise ValueError(msg)
        return df[col_name]
    return Expression(func, f'col({col_name!r})')


def col(col_name: Hashable) -> Expression:


    return_value = col_original(col_name)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The return value is an instance of Expression and its string representation matches the label 'col_original(col_name)' where col_name is represented by its repr().
    assert isinstance(return_value, Expression) and str(return_value) == f"col_original({col_name!r})"

    return return_value
