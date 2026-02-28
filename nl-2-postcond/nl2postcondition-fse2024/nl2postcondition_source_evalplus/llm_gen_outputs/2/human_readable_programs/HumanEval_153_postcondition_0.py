# The postcondition verifies that return_value consists of class_name and the strongest extension (CAP - SM) joined by a dot, selecting the first one in the list in case of ties.
assert return_value == class_name + "." + max(extensions, key=lambda s: sum(1 for c in s if c.isupper()) - sum(1 for c in s if c.islower()))


