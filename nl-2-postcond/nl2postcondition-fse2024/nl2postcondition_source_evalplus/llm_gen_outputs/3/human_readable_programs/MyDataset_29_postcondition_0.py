# The postcondition verifies that return_value is True if and only if the input obj is an instance of numbers.Number or np.number.
from numbers import Number
import numpy as np
assert return_value == isinstance(obj, (Number, np.number))


