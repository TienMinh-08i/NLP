# For each index i, return_value[i] is True if and only if the element at index i is not masked and has an unmasked duplicate elsewhere in values, with the 'keep' parameter determining whether it must be a previous occurrence ('first'), a subsequent occurrence ('last'), or any other occurrence (False).
assert all(
    return_value[i] == (
        not (mask[i] if mask is not None else False) and
        any(
            not (mask[j] if mask is not None else False) and 
            (values[i] == values[j] or (values[i] != values[i] and values[j] != values[j]))
            for j in (
                range(i) if keep == "first" else
                range(i + 1, len(values)) if keep == "last" else
                (k for k in range(len(values)) if k != i)
            )
        )
    )
    for i in range(len(values))
)


