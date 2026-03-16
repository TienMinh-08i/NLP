
# Response 0
# The return_value is a boolean array of the same length as comps, where each element is True if the corresponding element in comps is present in values (treating NaNs and NAs as equal), and False otherwise.
assert len(return_value) == len(list(comps)) and all(res == any((c is v) or (c == v) is True or (c != c and v != v) is True for v in list(values)) for res, c in zip(return_value, list(comps)))


