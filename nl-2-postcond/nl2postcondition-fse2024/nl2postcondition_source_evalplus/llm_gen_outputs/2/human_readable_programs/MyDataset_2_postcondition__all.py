
# Response 0
# The postcondition ensures that return_value is a boolean array of the same length as values, where each return_value[i] is True if and only if values[i] is not masked and there exists a non-masked values[j] equal to values[i] (treating NaNs as equal) such that j < i for keep='first', j > i for keep='last', or j != i for keep=False.
assert len(return_value) == len(values) and all(return_value[i] == (not (mask[i] if mask is not None else False) and any(not (mask[j] if mask is not None else False) and (values[i] == values[j] or (values[i] != values[i] and values[j] != values[j])) for j in range(len(values)) if (i != j and (keep is False or (keep == 'first' and j < i) or (keep == 'last' and j > i))))) for i in range(len(values)))


