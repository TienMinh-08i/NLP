
# Response 0
# The postcondition verifies that the return value is a tuple where the first element is the count of even digits ('0', '2', '4', '6', '8') and the second element is the count of odd digits ('1', '3', '5', '7', '9') found in the string representation of the integer num.
assert return_value == (len(list(filter(lambda ch: ch in "02468", str(num)))), len(list(filter(lambda ch: ch in "13579", str(num)))))


