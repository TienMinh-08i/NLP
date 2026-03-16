# The postcondition verifies that the return value is True if and only if the input object is list-like and has a "dtype" attribute.
assert return_value == (is_list_like(obj) and hasattr(obj, "dtype"))


