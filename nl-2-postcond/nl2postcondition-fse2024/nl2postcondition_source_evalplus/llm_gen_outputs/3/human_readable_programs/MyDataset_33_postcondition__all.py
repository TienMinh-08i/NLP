
# Response 0
# The return value is a list of mappings with length equal to the number of rows if orient is "records", otherwise it is a mapping of the type specified by into.
assert (isinstance(return_value, list) and len(return_value) == len(df) and all(map(lambda x: isinstance(x, (into if isinstance(into, type) else type(into))), return_value))) if orient == "records" else isinstance(return_value, (into if isinstance(into, type) else type(into)))


